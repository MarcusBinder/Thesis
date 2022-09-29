import gym
import numpy as np
from td3_torch import Agent
from utils_min import plot_learning_curve
from Custom_functions import CustomEnv2
import os

if __name__ == '__main__':
    SEED = 4
    FOLDER = "models/TD3_1"

    #env = gym.make('BipedalWalker-v2')
    env = CustomEnv2(t_steps = 5, dist = 5, nx = 3, ny = 3,
                    turb_type = 'nrel_5MW', combination = 'sosfs', deflection = 'gauss',
                    turbulence = 'crespo_hernandez', velocity = 'gauss',
                    WS_min = 7, WS_max = 7, TI_min = 0.07, TI_max = 0.07, wd_min = 270, wd_max = 315, 
                    yaw_max = 30, rho = 1.225, seed = SEED)
    
    agent = Agent(alpha=0.001, beta=0.001, 
                input_dims=env.observation_space.shape, tau=0.005,
                env=env, batch_size=100, layer1_size=400, layer2_size=300,
                n_actions=env.action_space.shape[0], seed=SEED ,folder=FOLDER)

    n_games = 1000
    filename = 'Floris_' + str(n_games) + 'games.png'

    figure_file = 'plots/' + filename

    best_score = env.reward_range[0]
    score_history = []

    #agent.load_models()

    for i in range(n_games):
        observation = env.reset()
        done = False
        score = 0
        while not done:
            action = agent.choose_action(observation)
            observation_, reward, done, info = env.step(action)
            agent.remember(observation, action, reward, observation_, done)
            agent.learn()
            score += reward
            observation = observation_
        score_history.append(score)
        avg_score = np.mean(score_history[-100:])

        if avg_score > best_score:
            best_score = avg_score
            agent.save_models()

        print('episode ', i, 'score %.2f' % score,
                'trailing 100 games avg %.3f' % avg_score)

    x = [i+1 for i in range(n_games)]
    plot_learning_curve(x, score_history, figure_file)

    #Save a score history to a csv file
    np.savetxt(FOLDER+"/score.csv", score_history, delimiter=',')
