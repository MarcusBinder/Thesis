# Thesis

# Note this
As some policy are stochastic by default (e.g. A2C or PPO), you should also try to set deterministic=True when calling the .predict() method, this frequently leads to better performance. Looking at the training curve (episode reward function of the timesteps) is a good proxy but underestimates the agent true performance.
From: https://stable-baselines.readthedocs.io/en/master/guide/rl_tips.html

It states that the training curve underestimates the agents true performance.


### Nomenclature
- MARL --  Multi agent reinforcement learning   

## Possible directions and problems to look into for the thesis

- Define the goal objective/goal function
	- Should it be just power output, or should load mitigation/damage be included 

- The first step would be to use MARL on a 3x3 farm on a single wind direction.
	- Look into MARL algorithms (IAC, MADDPG... )
	- Find and code implementation

Then, what comes next?
- Use GNN to simulate if a turbine is down for maintenance?
- Use transfer learning to optimize a slightly different farm layout? (square to rhomboid) 
- Use transfer learning to scale up the farm (3x3 -> 9x9)



Repositories used:
https://github.com/Farama-Foundation/PettingZoo
Maybe look into this, but I think petting zoo is fine
https://github.com/deepmind/acme




MARL PAPERS:
https://github.com/LantaoYu/MARL-Papers

To do list is:
[[Thesis Kanban]]

[[Text snippets]]


## [[Transfer learning]]



https://www.reddit.com/r/reinforcementlearning/comments/wx9akm/question_regarding_transfer_learning_with/

### MBPO
https://github.com/x35f/unstable_baselines
https://github.com/Xingyu-Lin/mbpo_pytorch
https://github.com/jannerm/mbpo

### Multiagent RL youtube videos to watch
[[Big list of yt videos]]



https://arxiv.org/abs/1709.06560

Old stuff:
[[Prethesis]]

$$ [J(\pi) = \int_{\tau} P(\tau|\pi) R(\tau) = \under{E} {\tau\sim \pi}{R(\tau)} $$