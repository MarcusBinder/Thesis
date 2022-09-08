import gym
import numpy as np
import os

from stable_baselines3 import PPO, A2C, SAC, TD3
from stable_baselines3.common.vec_env import DummyVecEnv, SubprocVecEnv
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.utils import set_random_seed
from stable_baselines3.common.env_checker import check_env
from stable_baselines3.common.noise import NormalActionNoise, OrnsteinUhlenbeckActionNoise

from Custom_functions import CustomEnv2


if __name__ == '__main__':

    #model_names = ["PPO4", "PPO5", "PPO6"]
    model_names = ["TD31", "TD32", "TD33"]
    SEEDS = [0, 3, 7]
 
    for model_name, SEED in zip(model_names, SEEDS):

        env = CustomEnv2(t_steps = 100, dist = 5, nx = 3, ny = 3,
                    turb_type = 'nrel_5MW', combination = 'sosfs', deflection = 'gauss',
                    turbulence = 'crespo_hernandez', velocity = 'gauss',
                    WS_min = 7, WS_max = 7, TI_min = 0.07, TI_max = 0.07, wd_min = 270, wd_max = 315, 
                    yaw_max = 30, rho = 1.225, seed = SEED)



        num_cpu = 2  # Number of processes to use
        env = make_vec_env(lambda: env, n_envs=num_cpu, seed=SEED, vec_env_cls=DummyVecEnv)

        # The noise objects for TD3
        n_actions = env.action_space.shape[-1]
        action_noise = NormalActionNoise(mean=np.zeros(n_actions), sigma=0.1 * np.ones(n_actions))

        #model = PPO("MlpPolicy", env, verbose=1, tensorboard_log='logs', seed = SEED)
        #model = A2C("MlpPolicy", env, verbose=1, tensorboard_log='logs', seed = SEED)
        #model = SAC("MlpPolicy", env, verbose=1, tensorboard_log='logs', seed = SEED, gradient_steps= -1)
        model = TD3("MlpPolicy", env, action_noise=action_noise,verbose=1, tensorboard_log='logs', seed = SEED, gradient_steps = -1, train_freq = 1)

        models_dir = "models/"+model_name
        log_dir = "logs"
    
        if not os.path.exists(models_dir):
            os.makedirs(models_dir)
            
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        TIMESTEPS = 25_000  #number timestep to save model

        print("Start learning")

        for i in range(1,20):
            model.learn(total_timesteps = TIMESTEPS, reset_num_timesteps = False, tb_log_name=model_name)
            model.save(f"{models_dir}/{TIMESTEPS*i}")
        
        del model

        print("Learning done")
    print("All done now!")
