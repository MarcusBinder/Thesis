import gym
import numpy as np
#from stable_baselines3 import A2C, DDPG, SAC, PPO
#from matplotlib import axis
import numpy as np
from floris.tools import FlorisInterface
#from floris.tools.visualization import visualize_cut_plane
#import matplotlib.pyplot as plt
#from floris.tools.optimization.yaw_optimization.yaw_optimizer_sr import YawOptimizationSR

from gym import spaces

#from stable_baselines3.common.env_checker import check_env
#import os
#import time
#from tqdm import tqdm_notebook
#from stable_baselines3.common.monitor import Monitor
#from stable_baselines3.common.results_plotter import load_results, ts2xy
#from stable_baselines3.common.noise import NormalActionNoise
#from stable_baselines3.common.callbacks import BaseCallback

#from stable_baselines3.common.vec_env import DummyVecEnv, SubprocVecEnv
#from stable_baselines3.common.env_util import make_vec_env
#from stable_baselines3.common.utils import set_random_seed

#from matplotlib.pyplot import figure

#loading optimization package:
#from scipy.optimize import minimize

# from floris.tools.optimization.yaw_optimization.yaw_optimizer_scipy import (
#     YawOptimizationScipy
# )

#from time import perf_counter as timerpc

import yaml
#import math
#from scipy import interpolate
import random


class CustomEnv(gym.Env):
    """
    The inputs are:
    t_steps     = number of timesteps pr simulation
    dist        ª= rotor diameters between the turbines
    nx          = number of turbines along x axis
    ny          = number of turbines along y axis
    turb_type   = The type of turbine used for the environment
    combination = The combination model
    deflection  = The deflection model
    turbulence  = The turbulence model
    velocity    = The wake velocity model
    VS_min      = minimum wind speed [m/s]
    VS_max      = maximum wind speed [m/s]
    TI_min      = minimum turbulence intensity
    TI_max      = maximum turbulence intensity
    wd_min      = minimum wind direction
    wd_max      = maximum wind direction
    yaw_max     = Is the maximum yaw offset allowed in degrees.
    
    """
    #Custom Environment that follows gym interface
    metadata = {'render.modes': ['human']}

    def __init__(self, t_steps = 10, dist = 5, nx = 3, ny = 3,
               turb_type = 'nrel_5MW', combination = 'sosfs', deflection = 'gauss',
               turbulence = 'crespo_hernandez', velocity = 'gauss',
               VS_min = 4, VS_max = 20, TI_min = 0.01, TI_max = 0.15, wd_min = 270, wd_max = 360, 
               yaw_max = 25, rho = 1.225, seed = 0):
        super(CustomEnv, self).__init__()
        
        random.seed(seed)
        np.random.seed(seed)
        
        self.t_max = t_steps   #The number of "simulations" pr episode.
        self.wind_speed_min = VS_min
        self.wind_speed_max = VS_max
        self.TI_min         = TI_min
        self.TI_max         = TI_max
        self.wd_min         = wd_min
        self.wd_max         = wd_max
        self.n_turb         = nx * ny
        self.yaw_max        = yaw_max
        self.rho            = rho
                     
        #Creates the base for the farm
        fi = FlorisInterface("gch.yaml")   
        
        #Turns it into a dictionary and then does the changes to the model
        fi_dict = fi.floris.as_dict()
        
        fi_dict["farm"]["turbine_type"] = [turb_type]
        fi_dict["wake"]["model_strings"]["combination_model"] = combination
        fi_dict["wake"]["model_strings"]["deflection_model"]  = deflection
        fi_dict["wake"]["model_strings"]["turbulence_model"]  = turbulence
        fi_dict["wake"]["model_strings"]["velocity_model"]    = velocity
        fi_dict["flow_field"]["air_density"]                  = rho
        
        # Turns it back into a floris object:
        self.fi = FlorisInterface(fi_dict)

        D = self.fi.floris.farm.rotor_diameters[0]

        x = np.linspace(0, D*dist*nx, nx)
        y = np.linspace(0, D*dist*ny, ny)

        xv, yv = np.meshgrid(x, y, indexing='xy')
        
        self.layout_x =  xv.flatten()
        self.layout_y = yv.flatten()
        
        #Reads and saves the power curve for one turbine:
        
        with open(turb_type+".yaml", 'r') as stream:
            try:
                parsed_yaml=yaml.safe_load(stream)
                #print(parsed_yaml)
            except yaml.YAMLError as exc:
                print(exc)

        ws_curve = parsed_yaml["power_thrust_table"]["wind_speed"]
        power_curve = parsed_yaml["power_thrust_table"]["power"]
        
        self.A = 3.14 * (D/2)**2
        self.power_curve = interpolate.interp1d(ws_curve, power_curve)
        

        # Define action and observation space
        
        # The actionspace is the 9 yaw angles.
        self.action_space = spaces.Box(low=-1, high=1,
                                            shape=(nx*ny,), dtype=np.float32)
        
        # The observationspace is WD, WS, TI:
        
        high = np.array([1, 1, 1], dtype = np.float32)
        low = np.array([0, 0, 0], dtype = np.float32)

        self.observation_space = spaces.Box(low, high, dtype=np.float32)

        self.reset()
        
    def step(self, action):
        #print("we did a step")
        if self.time >= self.t_max:
            done =  True
        else:
            self.time += 1
            done = False
            
        self.fi.calculate_wake(yaw_angles=np.array([[action]]))  #weird format, but it's okay
        
        power_farm = self.fi.get_farm_power()[0][0]
        
        #Choose if you want ideal farm, or greedy farm for reward calculation.
        #rew = self.fi.get_farm_power()/self.power_ideal_farm
        
        #Calculates the pct increase in power!
        increase = power_farm - self.power_greedy_farm[0][0]
        rew = (increase/self.power_greedy_farm[0][0])*100
        
        #rew = (self.fi.get_farm_power()/self.power_greey_farm-1)*1000   #old reward
        
        reward = rew  
            
        info = {}
        observation = np.array([self.wd_norm, self.ws_norm, self.TI_norm], dtype = np.float32)
        return observation, reward, done, info
    
    def reset(self):
        
        #
        self.ws = np.random.uniform(self.wind_speed_min, self.wind_speed_max)
        self.wd = np.random.uniform(self.wd_min, self.wd_max)
        self.TI = np.random.uniform(self.TI_min, self.TI_max)
        
        self.ws_norm = (self.ws - self.wind_speed_min)/(self.wind_speed_max - self.wind_speed_min)
        self.wd_norm = (self.wd - self.wd_min)/(self.wd_max - self.wd_min)
        self.TI_norm = (self.TI - self.TI_min)/(self.TI_max - self.TI_min)  
        
        self.fi.reinitialize(
            layout=(self.layout_x, self.layout_y),
            wind_directions=[self.wd],
            turbulence_intensity= self.TI,
            wind_speeds=[self.ws]
            )
        
        
        #Calculate greedy power. Used for normalization
        self.fi.calculate_wake()
        self.power_greedy_farm = self.fi.get_farm_power()
        
        #calculate the power for the ideal farm. Used for normalization
        # self.power_ideal_farm = self.power_curve(self.ws)*self.n_turb* (1/2) * self.rho * self.A * self.ws**3
        
        self.time = 0
        done = False
        
        observation = np.array([self.wd_norm, self.ws_norm, self.TI_norm], dtype = np.float32)
        return observation  # reward, done, info can't be included
    
    def render(self, mode='human'):
        pass
    
    def close (self):
        pass


class CustomEnv2(gym.Env):
    """
    The inputs are:
    t_steps     = number of timesteps pr simulation
    dist        ª= rotor diameters between the turbines
    nx          = number of turbines along x axis
    ny          = number of turbines along y axis
    turb_type   = The type of turbine used for the environment
    combination = The combination model
    deflection  = The deflection model
    turbulence  = The turbulence model
    velocity    = The wake velocity model
    VS_min      = minimum wind speed [m/s]
    VS_max      = maximum wind speed [m/s]
    TI_min      = minimum turbulence intensity
    TI_max      = maximum turbulence intensity
    wd_min      = minimum wind direction
    wd_max      = maximum wind direction
    yaw_max     = Is the maximum yaw offset allowed in degrees.
    
    """
    #Custom Environment that follows gym interface
    metadata = {'render.modes': ['human']}

    def __init__(self, t_steps = 10, dist = 5, nx = 3, ny = 3,
               turb_type = 'nrel_5MW', combination = 'sosfs', deflection = 'gauss',
               turbulence = 'crespo_hernandez', velocity = 'gauss',
               WS_min = 4, WS_max = 20, TI_min = 0.01, TI_max = 0.15, wd_min = 270, wd_max = 360, 
               yaw_max = 25, rho = 1.225, seed = 0):
        super(CustomEnv2, self).__init__()
        
        self.ws_range_min = 2
        self.ws_range_max = 20

        self.ti_range_min = 0.0
        self.ti_range_max = 0.20
        
        self.wd_range_min = 0
        self.wd_range_max = 360
        
        self.SEED = seed

        self.t_max = t_steps   #The number of "simulations" pr episode.
        self.wind_speed_min = WS_min
        self.wind_speed_max = WS_max
        self.TI_min         = TI_min
        self.TI_max         = TI_max
        self.wd_min         = wd_min
        self.wd_max         = wd_max
        self.n_turb         = nx * ny
        self.yaw_max        = yaw_max
        self.rho            = rho
                     
        #Creates the base for the farm
        fi = FlorisInterface("gch.yaml")   
        
        #Turns it into a dictionary and then does the changes to the model
        fi_dict = fi.floris.as_dict()
        
        fi_dict["farm"]["turbine_type"] = [turb_type]
        fi_dict["wake"]["model_strings"]["combination_model"] = combination
        fi_dict["wake"]["model_strings"]["deflection_model"]  = deflection
        fi_dict["wake"]["model_strings"]["turbulence_model"]  = turbulence
        fi_dict["wake"]["model_strings"]["velocity_model"]    = velocity
        fi_dict["flow_field"]["air_density"]                  = rho
        
        # Turns it back into a floris object:
        self.fi = FlorisInterface(fi_dict)

        D = self.fi.floris.farm.rotor_diameters[0]

        x = np.linspace(0, D*dist*nx, nx)
        y = np.linspace(0, D*dist*ny, ny)

        xv, yv = np.meshgrid(x, y, indexing='xy')
        
        self.layout_x =  xv.flatten()
        self.layout_y = yv.flatten()
        
        
        # The actionspace is the 9 yaw angles.
        self.action_space = spaces.Box(low=-1, high=1,
                                            shape=(nx*ny,), dtype=np.float32)
        

        
        high = np.array([1, 1, 1], dtype = np.float32)
        low = np.array([0, 0, 0], dtype = np.float32)

        self.observation_space = spaces.Box(low, high, dtype=np.float32)

        self.reset()
        
    def step(self, action):
        #print("we did a step")
        if self.time >= self.t_max:
            done =  True
        else:
            self.time += 1
            done = False

        self.ws = np.random.uniform(self.wind_speed_min, self.wind_speed_max)
        self.wd = np.random.uniform(self.wd_min, self.wd_max)
        self.TI = np.random.uniform(self.TI_min, self.TI_max)
        
        self.ws_norm = (self.ws - self.ws_range_min)/(self.ws_range_max - self.ws_range_min)
        self.wd_norm = (self.wd - self.wd_range_min)/(self.wd_range_max - self.wd_range_min)
        self.TI_norm = (self.TI - self.ti_range_min)/(self.ti_range_max - self.ti_range_min)  
        
        self.fi.reinitialize(
            layout=(self.layout_x, self.layout_y),
            wind_directions=[self.wd],
            turbulence_intensity= self.TI,
            wind_speeds=[self.ws]
            )
        
        
        #Calculate greedy power. Used for normalization
        self.fi.calculate_wake()
        self.power_greedy_farm = self.fi.get_farm_power()[0][0]

        self.fi.calculate_wake(yaw_angles=np.array([[action*self.yaw_max]]))  
        
        self.power_agent_farm = self.fi.get_farm_power()[0][0]
        
        #Calculates the pct increase in power!
        increase = self.power_agent_farm - self.power_greedy_farm
        
        reward = (increase/self.power_greedy_farm)*100
            
        info = {}
        # The observationspace is WD, WS, TI:
        observation = np.array([self.wd_norm, self.ws_norm, self.TI_norm], dtype = np.float32)
        return observation, reward, done, info
    
    def reset(self):
        
        random.seed(self.SEED)
        np.random.seed(self.SEED)

        #
        self.ws = np.random.uniform(self.wind_speed_min, self.wind_speed_max)
        self.wd = np.random.uniform(self.wd_min, self.wd_max)
        self.TI = np.random.uniform(self.TI_min, self.TI_max)
        
        self.ws_norm = (self.ws - self.ws_range_min)/(self.ws_range_max - self.ws_range_min)
        self.wd_norm = (self.wd - self.wd_range_min)/(self.wd_range_max - self.wd_range_min)
        self.TI_norm = (self.TI - self.ti_range_min)/(self.ti_range_max - self.ti_range_min)  
        
        self.fi.reinitialize(
            layout=(self.layout_x, self.layout_y),
            wind_directions=[self.wd],
            turbulence_intensity= self.TI,
            wind_speeds=[self.ws]
            )
        
        
        #Calculate greedy power. Used for normalization
        #self.fi.calculate_wake()
        #self.power_greedy_farm = self.fi.get_farm_power()
        
        self.time = 0
        done = False
        
        observation = np.array([self.wd_norm, self.ws_norm, self.TI_norm], dtype = np.float32)
        return observation  # reward, done, info can't be included
    
    def render(self, mode='human'):
        pass
    
    def close (self):
        pass