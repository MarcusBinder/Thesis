import gym
import numpy as np
import os

from stable_baselines3 import PPO, A2C
from stable_baselines3.common.vec_env import DummyVecEnv, SubprocVecEnv
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.utils import set_random_seed
from stable_baselines3.common.env_checker import check_env

from Custom_functions import CustomEnv9


if __name__ == '__main__':

    #model_names = ["PPO1", "PPO2"]
    model_names = ["A2C33", "A2C34"]
    SEEDS = [0, 42]
 
    for model_name, SEED in zip(model_names, SEEDS):

        env = CustomEnv9(t_steps = 100, dist = 5, nx = 2, ny = 2,
                    turb_type = 'nrel_5MW', combination = 'sosfs', deflection = 'gauss',
                    turbulence = 'crespo_hernandez', velocity = 'gauss', wd_possible = (270, 285, 300, 315, 330, 345, 360),
                    yaw_max = 30, rho = 1.225, seed = SEED)


        num_cpu = 4  # Number of processes to use
        env = make_vec_env(lambda: env, n_envs=num_cpu, seed=SEED, vec_env_cls=DummyVecEnv)

        #model = PPO("MlpPolicy", env, verbose=1, tensorboard_log='logs', seed = SEED)
        model = A2C("MlpPolicy", env, verbose=1, tensorboard_log='logs', seed = SEED)
    
        models_dir = "models/"+model_name
        log_dir = "logs"
    
        if not os.path.exists(models_dir):
            os.makedirs(models_dir)
            
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        TIMESTEPS = 10_000  #number timestep to save model

        print("Start learning")

        for i in range(1,150+1):
            model.learn(total_timesteps = TIMESTEPS, reset_num_timesteps = False, tb_log_name=model_name)
            model.save(f"{models_dir}/{TIMESTEPS*i}")
        
        del model

        print("Learning done")
    print("All done now!")
