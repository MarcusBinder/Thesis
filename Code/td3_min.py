import os
import copy

import torch as T
import torch.nn.functional as F
import torch.nn as nn

import numpy as np
from buffer import ReplayBuffer
#from networks import ActorNetwork, CriticNetwork
import random




class Actor(nn.Module):
    #This is the actor class. Note that the forward method gives tanh, so it is bounded between -1 and 1
	def __init__(self, input_dims, n_actions, l1_dims, l2_dims):
		super(Actor, self).__init__()

		self.l1 = nn.Linear(input_dims, l1_dims)
		self.l2 = nn.Linear(l1_dims, l2_dims)
		self.l3 = nn.Linear(l2_dims, n_actions)
		
	def forward(self, state):
		a = F.relu(self.l1(state))
		a = F.relu(self.l2(a))
		return T.tanh(self.l3(a))



class Critic(nn.Module):
    #Critic module.
	def __init__(self, input_dims, n_actions, l1_dims, l2_dims):
		super(Critic, self).__init__()

		# Critic 1
		self.l1 = nn.Linear(input_dims + n_actions, l1_dims)
		self.l2 = nn.Linear(l1_dims, l2_dims)
		self.l3 = nn.Linear(l2_dims, 1)

		# Critic 2
		self.l4 = nn.Linear(input_dims + n_actions, l1_dims)
		self.l5 = nn.Linear(l1_dims, l2_dims)
		self.l6 = nn.Linear(l2_dims, 1)


	def forward(self, state, action):
        #does the forward method. Note that we have 2 networks in one.

		state_action = T.cat([state, action], dim=1)

		q1 = F.relu(self.l1(state_action))
		q1 = F.relu(self.l2(q1))
		q1 = self.l3(q1)

		q2 = F.relu(self.l4(state_action))
		q2 = F.relu(self.l5(q2))
		q2 = self.l6(q2)
		return q1, q2


	def Q1(self, state, action):
        #Gives the q1 value
		state_action = T.cat([state, action], dim=1)

		q1 = F.relu(self.l1(state_action))
		q1 = F.relu(self.l2(q1))
		q1 = self.l3(q1)
		return q1



class Agent():
    def __init__(self, alpha, beta, input_dims, tau, env,
            gamma=0.99, update_actor_interval=2, n_actions=2, layer1_size=400,
            layer2_size=300, seed = 42, folder = None, 
            policy_noise = 0.2, noise_clip = 0.5):
        self.gamma = gamma
        self.tau = tau
        self.max_action = env.action_space.high
        self.min_action = env.action_space.low
        self.learn_step_cntr = 0
        self.time_step = 0
        self.n_actions = n_actions
        self.update_actor_iter = update_actor_interval
        self.device = T.device("cuda" if T.cuda.is_available() else "cpu")
        self.policy_noise = policy_noise
        self.noise_clip = noise_clip

        self.set_seed(seed)

        if folder is not None:
            # If the folder is specified, then we are not saving in tmp anymore.
            #create folder.
            if not os.path.exists(folder):
                os.makedirs(folder)

        # Initializes the actor and critic networks.
        self.actor = Actor(input_dims, n_actions, l1_dims=layer1_size, l2_dims=layer2_size).to(self.device)
        self.actor_target = copy.deepcopy(self.actor)
        self.actor_optimizer = T.optim.Adam(self.actor.parameters(), lr=alpha)

        self.critic = Critic(input_dims, n_actions, l1_dims=layer1_size, l2_dims=layer2_size).to(self.device)
        self.critic_target = copy.deepcopy(self.critic)
        self.critic_optimizer = T.optim.Adam(self.critic.parameters(), lr=beta)


    def choose_action(self, observation):
        """
        From an observation, chooses an action.
        """
        state = T.tensor(observation, dtype=T.float).to(self.device)

        mu = self.actor.forward(state).to(self.device)

        return mu.cpu().detach().numpy()  


    def learn(self, replay_buffer, batch_size=256):
        """
        This is the learn function for the agent.
        """

        self.learn_step_cntr += 1

        #First we sample the replay buffer.
        state, action, new_state, reward, not_done = replay_buffer.sample(batch_size)

        with  T.no_grad():
            #select the action, with noise added.
            noise = T.clamp(T.randn_like(action) * self.policy_noise, min=self.noise_clip, max=self.noise_clip)  #Create and clamp the noise
            next_action = T.clamp(self.actor_target(new_state) + noise, min=self.min_action[0], max=self.max_action[0]) #Adds the noise to the target action, and clamps it.
            
            # Calculate the target Q value.
            target_Q1, target_Q2 = self.critic_target(new_state, next_action)
            target_Q = T.min(target_Q1, target_Q2)  #Select the min. this is the critic value.
            target_Q = reward + not_done * self.gamma * target_Q

        current_Q1, current_Q2 = self.critic(state, action)

        # Compute critic loss
        critic_loss = F.mse_loss(current_Q1, target_Q) + F.mse_loss(current_Q2, target_Q)  #the loss is the sum of the MSE loss

		# Optimize the critic
        self.critic_optimizer.zero_grad()
        critic_loss.backward()
        self.critic_optimizer.step()
        

        if self.learn_step_cntr % self.update_actor_iter == 0:
            #only update the polycy every x time.

            # Compute actor losse
            actor_loss = -T.mean(self.critic.Q1(state, self.actor(state)))

            # Optimize the actor 
            self.actor_optimizer.zero_grad()
            actor_loss.backward()
            self.actor_optimizer.step()

            # Now for updating the network parameters.
            # this does the polyac averaging.
            for param, target_param in zip(self.critic.parameters(), self.critic_target.parameters()):
                target_param.data.copy_(self.tau * param.data + (1 - self.tau) * target_param.data)

            for param, target_param in zip(self.actor.parameters(), self.actor_target.parameters()):
                target_param.data.copy_(self.tau * param.data + (1 - self.tau) * target_param.data)

    def save(self, filename, extra):
        #print("saving model")
        T.save(self.critic.state_dict(), filename + "_critic_" + str(extra))
        #T.save(self.critic_optimizer.state_dict(), filename + "_critic_optimizer")

        T.save(self.actor.state_dict(), filename + "_actor_" + str(extra))
        #T.save(self.actor_optimizer.state_dict(), filename + "_actor_optimizer")


    def load(self, filename, extra):
        self.critic.load_state_dict(T.load(filename + "_critic_" + str(extra)))
        #self.critic_optimizer.load_state_dict(T.load(filename + "_critic_optimizer"))
        self.critic_target = copy.deepcopy(self.critic)

        self.actor.load_state_dict(T.load(filename + "_actor_" + str(extra)))
        #self.actor_optimizer.load_state_dict(T.load(filename + "_actor_optimizer"))
        self.actor_target = copy.deepcopy(self.actor)
    
    def set_seed(self, seed):
        """
        Sets the random seed.
        """
        # Seed python RNG
        random.seed(seed)
        # Seed numpy RNG
        np.random.seed(seed)
        # seed the RNG for all devices (both CPU and CUDA)
        T.manual_seed(seed)



class ReplayBuffer(object):
	def __init__(self, state_dim, action_dim, max_size=int(1e6)):
		self.max_size = max_size
		self.ptr = 0
		self.size = 0

		self.state = np.zeros((max_size, state_dim))
		self.action = np.zeros((max_size, action_dim))
		self.next_state = np.zeros((max_size, state_dim))
		self.reward = np.zeros((max_size, 1))
		self.not_done = np.zeros((max_size, 1))

		self.device = T.device("cuda" if T.cuda.is_available() else "cpu")


	def add(self, state, action, next_state, reward, done):
		self.state[self.ptr] = state
		self.action[self.ptr] = action
		self.next_state[self.ptr] = next_state
		self.reward[self.ptr] = reward
		self.not_done[self.ptr] = 1. - done

		self.ptr = (self.ptr + 1) % self.max_size
		self.size = min(self.size + 1, self.max_size)


	def sample(self, batch_size):
		ind = np.random.randint(0, self.size, size=batch_size)

		return (
			T.FloatTensor(self.state[ind]).to(self.device),
			T.FloatTensor(self.action[ind]).to(self.device),
			T.FloatTensor(self.next_state[ind]).to(self.device),
			T.FloatTensor(self.reward[ind]).to(self.device),
			T.FloatTensor(self.not_done[ind]).to(self.device)
		)