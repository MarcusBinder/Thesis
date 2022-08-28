# Spinning up notes
This is my place to store notes about the spinning up go through.
https://spinningup.openai.com/en/latest/spinningup/rl_intro.html

## Part 1. Key Concepts in RL

In a nutshell, RL is the study of agents and how they learn by trial and error. It formalizes the idea that rewarding or punishing an agent for its behavior makes it more likely to repeat or forego that behavior in the future.
![[Pasted image 20220826192509.png]]

### States and observations
A **state** $s$ is a complete description of the world. No information about the world is hidden in the state.
An **observation** $o$ is a partial description of a state, that may omit some information.

States and observations are represented by a vector, matrix or a tensor.  The state of a robot might be represented by its joint angles and velocities.

The environment can be **fully observed** if we can observe the complete state, or it van be **partially observed**

### Action spaces
The action space is different depending on the environment. It can be *discrete* or *continuous*. Note that some algorithms only work for on case, and would need to be substantially reworked for other cases.

### Policies
The **policy** is the rule that an agent uses to decide what action to take. It can be *deterministic*. In that case it is denoted by $\mu$
$$
a_t = \mu(s_t)
$$
If it is *stochastic*, it is denoted by $\pi$
$$
a_t \sim \pi(\cdot|s_t)
$$
As the policy is the "brain" of the agent, these two words are somewhat interchangeable.


### Trajectories
A trajectory $\tau$ is the sequence of states and actions in the world
$$
\tau = (s_0,a_0,s_1,a_1,\dots)
$$
The first state $s_0$ is randomly sampled from the **start-state distribution**, which is sometimes denoted by $\rho_0$
$$
s_0 \sim \rho_0(\cdot)
$$
State transitions is what happens between the state at a time $t$, $s_t$ and the next state at $t+1$, $s_{t+1}$. They are governed by the natural laws of the environment, and only depend on the most recent action $a_t$. If they are deterministic:
$$
s_{t+1} = f(s_t,a_t)
$$
Or if they are stochastic:
$$
s_{t+1} \sim P(\cdot|s_t,a_t)
$$
The actions are chosen by the agent according to its policy

Note that trajectories are also called **episodes** or **rollouts**

### Reward and return
The reward function $R$ is *very* important in reinforcement learning! It depends on the current state, the action taken and the next state
$$
r_t = R(s_t,a_t,s_{t+1})
$$
Note this is often simplifies to $r_t = R(s_t)$ or $r_t = R(s_t,a_t)$

The agent want to maximize its cumulative reward, over its **trajectory**. There are different formulations for this reward. It van be **finite-horizon undiscounted return**, that is simply the return of the rewards:
$$
R(\tau) = \sum_{t=0}^T r_t
$$
It can also be the **infinite-horizon discounted return**. Here the future rewards are discounted by how far they are in the future by the factor $\gamma \in(0,1)$ 
$$
R(\tau) = \sum_{t=0}^\infty \gamma ^ t r_t
$$
Note that an infinite-horizon sum of rewards [may not converge](https://en.wikipedia.org/wiki/Convergent_series) to a finite value, and is hard to deal with in equations. But with a discount factor and under reasonable conditions, the infinite sum converges.



### RL optimization problem
The goal in RL is to select a policy which maximizes **expected return** when the agent acts according to it.
If the environment transitions and the policy are stochastic, the probability of a T-step trajectory is:
$$P(\tau|\pi) = \rho_0 (s_0) \prod_{t=0}^{T-1} P(s_{t+1} | s_t, a_t) \pi(a_t | s_t). $$
The expected return is denoted by $J(\pi)$ and is:
$$ J(\pi) = \int_{\tau} P(\tau|\pi) R(\tau) = E_{\tau\sim \pi} [{R(\tau)}] $$
The central optimization problem in RL can then be expressed by

$$ \pi^* = \arg \max_{\pi} J(\pi) $$

Where $\pi^*$ is the **optimal policy**

### Value function
So we want to know the **value** of a state, or state action pair. 
Note that value is the expected return if we start in a given state, and then act according to the policy afterwards. 
There are four main functions:
1) The **On-policy Value Function** $V^\pi(s)$. This gives the expected return, if we start in state $s$ and always act according to policy $\pi$
$$V^{\pi}(s) = E_{\tau \sim \pi}{[R(\tau)\left| s_0 = s\right.}]$$

2) The **On-policy Action-value function** $Q^\pi(s,a)$ which gives the expected return if you start in state $s$ take an arbitrary action $a$ (which may not have come from the policy), and then forever after act according to policy $\pi$
$$
Q^{\pi}(s,a) = E_{\tau \sim \pi}[{R(\tau)\left| s_0 = s, a_0 = a\right.} ]
$$

3) The **Optimal Value Function** $V^*(s)$ which gives the expected return if you start in state $s$ and always act according to the *optimal* policy in the environment
$$V^{*}(s) =\max_{\pi} E_{\tau \sim \pi}{[R(\tau)\left| s_0 = s\right.}]$$

4) The **Optimal Action Value function** $Q^*(s,a)$ which gives the expected return if you start in state $s$, take an arbitrary action $a$, and then forever after act according to the _optimal_ policy in the environment:
$$
Q^{*}(s,a) = \max_\pi E_{\tau \sim \pi}[{R(\tau)\left| s_0 = s, a_0 = a\right.} ]
$$

https://spinningup.openai.com/en/latest/spinningup/rl_intro.html