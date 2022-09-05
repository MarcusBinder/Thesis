import gym
import numpy as np
import os

from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv, SubprocVecEnv
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.utils import set_random_seed
from stable_baselines3.common.env_checker import check_env

from Custom_functions import CustomEnv


if __name__ == '__main__':

    model_name = "PPO_test_cluster"
    SEED = 0

    env = CustomEnv(t_steps = 10, dist = 5, nx = 3, ny = 3,
               turb_type = 'nrel_5MW', combination = 'sosfs', deflection = 'gauss',
               turbulence = 'crespo_hernandez', velocity = 'gauss',
               VS_min = 4, VS_max = 15, TI_min = 0.07, TI_max = 0.07, wd_min = 270, wd_max = 315, 
               yaw_max = 25, rho = 1.225, seed = SEED)



    #env_id = "CartPole-v1"
    num_cpu = 4  # Number of processes to use
    # Create the vectorized environment
    # env = SubprocVecEnv([make_env(env_id, i) for i in range(num_cpu)])
    # Stable Baselines provides you with make_vec_env() helper
    # which does exactly the previous steps for you.
    # You can choose between `DummyVecEnv` (usually faster) and `SubprocVecEnv`
    env = make_vec_env(lambda: env, n_envs=num_cpu, seed=0, vec_env_cls=DummyVecEnv)

    model = PPO("MlpPolicy", env, verbose=1, tensorboard_log='logs', seed = SEED)
    
    models_dir = "models/"+model_name
    log_dir = "logs"
    
    if not os.path.exists(models_dir):
        os.makedirs(models_dir)
        
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    TIMESTEPS = 1_000  #number timestep to save model

    print("Start learning")

    for i in range(1,3):
        model.learn(total_timesteps = TIMESTEPS, reset_num_timesteps = False, tb_log_name=model_name)
        model.save(f"{models_dir}/{TIMESTEPS*i}")
    
    print("Learning done")
    
