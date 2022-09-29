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
import copy

#from time import perf_counter as timerpc

import yaml
#import math
#from scipy import interpolate
import random


# class CustomEnv(gym.Env):
#     """
#     The inputs are:
#     t_steps     = number of timesteps pr simulation
#     dist        ª= rotor diameters between the turbines
#     nx          = number of turbines along x axis
#     ny          = number of turbines along y axis
#     turb_type   = The type of turbine used for the environment
#     combination = The combination model
#     deflection  = The deflection model
#     turbulence  = The turbulence model
#     velocity    = The wake velocity model
#     VS_min      = minimum wind speed [m/s]
#     VS_max      = maximum wind speed [m/s]
#     TI_min      = minimum turbulence intensity
#     TI_max      = maximum turbulence intensity
#     wd_min      = minimum wind direction
#     wd_max      = maximum wind direction
#     yaw_max     = Is the maximum yaw offset allowed in degrees.
    
#     """
#     #Custom Environment that follows gym interface
#     metadata = {'render.modes': ['human']}

#     def __init__(self, t_steps = 10, dist = 5, nx = 3, ny = 3,
#                turb_type = 'nrel_5MW', combination = 'sosfs', deflection = 'gauss',
#                turbulence = 'crespo_hernandez', velocity = 'gauss',
#                VS_min = 4, VS_max = 20, TI_min = 0.01, TI_max = 0.15, wd_min = 270, wd_max = 360, 
#                yaw_max = 25, rho = 1.225, seed = 0):
#         super(CustomEnv, self).__init__()
        
#         random.seed(seed)
#         np.random.seed(seed)
        
#         self.t_max = t_steps   #The number of "simulations" pr episode.
#         self.wind_speed_min = VS_min
#         self.wind_speed_max = VS_max
#         self.TI_min         = TI_min
#         self.TI_max         = TI_max
#         self.wd_min         = wd_min
#         self.wd_max         = wd_max
#         self.n_turb         = nx * ny
#         self.yaw_max        = yaw_max
#         self.rho            = rho
                     
#         #Creates the base for the farm
#         fi = FlorisInterface("gch.yaml")   
        
#         #Turns it into a dictionary and then does the changes to the model
#         fi_dict = fi.floris.as_dict()
        
#         fi_dict["farm"]["turbine_type"] = [turb_type]
#         fi_dict["wake"]["model_strings"]["combination_model"] = combination
#         fi_dict["wake"]["model_strings"]["deflection_model"]  = deflection
#         fi_dict["wake"]["model_strings"]["turbulence_model"]  = turbulence
#         fi_dict["wake"]["model_strings"]["velocity_model"]    = velocity
#         fi_dict["flow_field"]["air_density"]                  = rho
        
#         # Turns it back into a floris object:
#         self.fi = FlorisInterface(fi_dict)

#         D = self.fi.floris.farm.rotor_diameters[0]

#         x = np.linspace(0, D*dist*nx, nx)
#         y = np.linspace(0, D*dist*ny, ny)

#         xv, yv = np.meshgrid(x, y, indexing='xy')
        
#         self.layout_x =  xv.flatten()
#         self.layout_y = yv.flatten()
        
#         #Reads and saves the power curve for one turbine:
        
#         with open(turb_type+".yaml", 'r') as stream:
#             try:
#                 parsed_yaml=yaml.safe_load(stream)
#                 #print(parsed_yaml)
#             except yaml.YAMLError as exc:
#                 print(exc)

#         ws_curve = parsed_yaml["power_thrust_table"]["wind_speed"]
#         power_curve = parsed_yaml["power_thrust_table"]["power"]
        
#         self.A = 3.14 * (D/2)**2
#         self.power_curve = interpolate.interp1d(ws_curve, power_curve)
        

#         # Define action and observation space
        
#         # The actionspace is the 9 yaw angles.
#         self.action_space = spaces.Box(low=-1, high=1,
#                                             shape=(nx*ny,), dtype=np.float32)
        
#         # The observationspace is WD, WS, TI:
        
#         high = np.array([1, 1, 1], dtype = np.float32)
#         low = np.array([0, 0, 0], dtype = np.float32)

#         self.observation_space = spaces.Box(low, high, dtype=np.float32)

#         self.reset()
        
#     def step(self, action):
#         #print("we did a step")
#         if self.time >= self.t_max:
#             done =  True
#         else:
#             self.time += 1
#             done = False
            
#         self.fi.calculate_wake(yaw_angles=np.array([[action]]))  #weird format, but it's okay
        
#         power_farm = self.fi.get_farm_power()[0][0]
        
#         #Choose if you want ideal farm, or greedy farm for reward calculation.
#         #rew = self.fi.get_farm_power()/self.power_ideal_farm
        
#         #Calculates the pct increase in power!
#         increase = power_farm - self.power_greedy_farm[0][0]
#         rew = (increase/self.power_greedy_farm[0][0])*100
        
#         #rew = (self.fi.get_farm_power()/self.power_greey_farm-1)*1000   #old reward
        
#         reward = rew  
            
#         info = {}
#         observation = np.array([self.wd_norm, self.ws_norm, self.TI_norm], dtype = np.float32)
#         return observation, reward, done, info
    
#     def reset(self):
        
#         #
#         self.ws = np.random.uniform(self.wind_speed_min, self.wind_speed_max)
#         self.wd = np.random.uniform(self.wd_min, self.wd_max)
#         self.TI = np.random.uniform(self.TI_min, self.TI_max)
        
#         self.ws_norm = (self.ws - self.wind_speed_min)/(self.wind_speed_max - self.wind_speed_min)
#         self.wd_norm = (self.wd - self.wd_min)/(self.wd_max - self.wd_min)
#         self.TI_norm = (self.TI - self.TI_min)/(self.TI_max - self.TI_min)  
        
#         self.fi.reinitialize(
#             layout=(self.layout_x, self.layout_y),
#             wind_directions=[self.wd],
#             turbulence_intensity= self.TI,
#             wind_speeds=[self.ws]
#             )
        
        
#         #Calculate greedy power. Used for normalization
#         self.fi.calculate_wake()
#         self.power_greedy_farm = self.fi.get_farm_power()
        
#         #calculate the power for the ideal farm. Used for normalization
#         # self.power_ideal_farm = self.power_curve(self.ws)*self.n_turb* (1/2) * self.rho * self.A * self.ws**3
        
#         self.time = 0
#         done = False
        
#         observation = np.array([self.wd_norm, self.ws_norm, self.TI_norm], dtype = np.float32)
#         return observation  # reward, done, info can't be included
    
#     def render(self, mode='human'):
#         pass
    
#     def close (self):
#         pass


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

        self.ws = np.round(np.random.uniform(self.wind_speed_min, self.wind_speed_max), decimals=1)
        self.wd = np.round(np.random.uniform(self.wd_min, self.wd_max), decimals=1)
        self.TI = np.random.uniform(self.TI_min, self.TI_max)

        obs_scaled = self.scale_obs(self.ws, self.wd, self.TI)
        
        # self.ws_norm = (self.ws - self.ws_range_min)/(self.ws_range_max - self.ws_range_min)
        # self.wd_norm = (self.wd - self.wd_range_min)/(self.wd_range_max - self.wd_range_min)
        # self.TI_norm = (self.TI - self.ti_range_min)/(self.ti_range_max - self.ti_range_min)  

        observation = obs_scaled #np.array([self.wd_norm, self.ws_norm, self.TI_norm], dtype = np.float32)

        return observation, reward, done, info
    
    def reset(self):
        
        random.seed(self.SEED)
        np.random.seed(self.SEED)

        #np.round(A,decimals=1)
        self.ws = np.round(np.random.uniform(self.wind_speed_min, self.wind_speed_max), decimals=1)
        self.wd = np.round(np.random.uniform(self.wd_min, self.wd_max), decimals=1)
        self.TI = np.random.uniform(self.TI_min, self.TI_max)
        
        obs_scaled = self.scale_obs(self.ws, self.wd, self.TI)

        
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
        
        observation = obs_scaled
        return observation  # reward, done, info can't be included

    def scale_obs(self, ws, wd, TI):
        #Takes inputs and scales them to the observation.

        self.ws_norm = (ws - self.ws_range_min)/(self.ws_range_max - self.ws_range_min)
        self.wd_norm = (wd - self.wd_range_min)/(self.wd_range_max - self.wd_range_min)
        self.TI_norm = (TI - self.ti_range_min)/(self.ti_range_max - self.ti_range_min)  

        obs_scaled = np.array([self.wd_norm, self.ws_norm, self.TI_norm], dtype = np.float32)
        return obs_scaled
    
    def render(self, mode='human'):
        pass
    
    def close (self):
        pass

    def change_seed(self, seed):
        self.seed = seed

# ##########################################################################################
# ##########################################################################################


# class CustomEnv3(gym.Env):
#     """
#     This is for stepwise changes in the wind conditions. Also the yaw is now part of the observation space.
#     The inputs are:
#     t_steps     = number of timesteps pr simulation
#     dist        = rotor diameters between the turbines
#     nx          = number of turbines along x axis
#     ny          = number of turbines along y axis
#     turb_type   = The type of turbine used for the environment
#     combination = The combination model
#     deflection  = The deflection model
#     turbulence  = The turbulence model
#     velocity    = The wake velocity model
#     VS_min      = minimum wind speed [m/s]
#     VS_max      = maximum wind speed [m/s]
#     TI_min      = minimum turbulence intensity
#     TI_max      = maximum turbulence intensity
#     wd_min      = minimum wind direction
#     wd_max      = maximum wind direction
#     yaw_max     = Is the maximum yaw offset allowed in degrees.
    
#     """
#     #Custom Environment that follows gym interface
#     metadata = {'render.modes': ['human']}

#     def __init__(self, t_steps = 100, dist = 5, nx = 3, ny = 3,
#                turb_type = 'nrel_5MW', combination = 'sosfs', deflection = 'gauss',
#                turbulence = 'crespo_hernandez', velocity = 'gauss',
#                WS_min = 4, WS_max = 20, TI_min = 0.01, TI_max = 0.15, wd_min = 270, wd_max = 360, 
#                yaw_max = 30, rho = 1.225, seed = 0):
#         super(CustomEnv3, self).__init__()
        
#         self.ws_range_min = 2
#         self.ws_range_max = 20

#         self.ti_range_min = 0.0
#         self.ti_range_max = 0.20
        
#         self.wd_range_min = 0
#         self.wd_range_max = 360
        
#         self.SEED = seed

#         self.t_max = t_steps   #The number of "simulations" pr episode.
#         #self.wind_speed_min = WS_min
#         #self.wind_speed_max = WS_max
#         #self.TI_min         = TI_min
#         #self.TI_max         = TI_max
#         #self.wd_min         = wd_min
#         #self.wd_max         = wd_max
#         self.n_turb         = nx * ny
#         self.yaw_max        = yaw_max
#         self.rho            = rho
                     
#         #Creates the base for the farm
#         fi = FlorisInterface("gch.yaml")   
        
#         #Turns it into a dictionary and then does the changes to the model
#         fi_dict = fi.floris.as_dict()
        
#         fi_dict["farm"]["turbine_type"] = [turb_type]
#         fi_dict["wake"]["model_strings"]["combination_model"] = combination
#         fi_dict["wake"]["model_strings"]["deflection_model"]  = deflection
#         fi_dict["wake"]["model_strings"]["turbulence_model"]  = turbulence
#         fi_dict["wake"]["model_strings"]["velocity_model"]    = velocity
#         fi_dict["flow_field"]["air_density"]                  = rho
        
#         # Turns it back into a floris object:
#         self.fi = FlorisInterface(fi_dict)

#         D = self.fi.floris.farm.rotor_diameters[0]

#         x = np.linspace(0, D*dist*nx, nx)
#         y = np.linspace(0, D*dist*ny, ny)

#         xv, yv = np.meshgrid(x, y, indexing='xy')
        
#         self.layout_x =  xv.flatten()
#         self.layout_y = yv.flatten()
        
        
#         # The actionspace is the 9 yaw angles.
#         self.action_space = spaces.Box(low=-1, high=1,
#                                             shape=(nx*ny,), dtype=np.float32)
        

#         self.observation_space = spaces.Box(low = -1, high = 1,
#                                             shape = (3 + nx*ny,), dtype=np.float32) #The observation spave is now: [wd, ws, TI, yaw angles.]

#         random.seed(self.SEED)
#         np.random.seed(self.SEED)
#         self.reset()
        
#     def step(self, action):

#         if self.time >= self.t_max:
#             done =  True
#         else:
#             self.time += 1
#             done = False

#         if 15 <= self.time <= 60:
#             #print("Changing wind direction")

#             self.wd += 1
#             self.yaw_current += 1


#         # self.ws = np.round(np.random.uniform(self.wind_speed_min, self.wind_speed_max), decimals=1)
#         # self.wd = np.round(np.random.uniform(self.wd_min, self.wd_max), decimals=1)
#         # self.TI = np.random.uniform(self.TI_min, self.TI_max)
        
#         # self.ws_norm = (self.ws - self.ws_range_min)/(self.ws_range_max - self.ws_range_min)
#         self.wd_norm = (self.wd - self.wd_range_min)/(self.wd_range_max - self.wd_range_min)
#         # self.TI_norm = (self.TI - self.ti_range_min)/(self.ti_range_max - self.ti_range_min)  
        
#         self.fi.reinitialize(
#             layout=(self.layout_x, self.layout_y),
#             wind_directions=[self.wd],
#             turbulence_intensity= self.TI,
#             wind_speeds=[self.ws]
#             )
        
#         self.yaw_current += action 
#         self.yaw_current = np.clip(self.yaw_current, -self.yaw_max, self.yaw_max)
#         self.yaw_current_norm = self.yaw_current/self.yaw_max   

#         if self.wd_last != self.wd:
#             #print("Now calculating new power")
#             #If wind direction has changed, then calculate a new power. 
#             #Calculate greedy power. Used for normalization
#             self.fi.calculate_wake()
#             self.power_greedy_farm = self.fi.get_farm_power()[0][0]

#         self.wd_last = copy.copy(self.wd)

#         self.fi.calculate_wake(yaw_angles=np.array([[self.yaw_current]]))  
        
#         self.power_agent_farm = self.fi.get_farm_power()[0][0]
        
#         #Calculates the pct increase in power!
#         increase = self.power_agent_farm - self.power_greedy_farm
        
#         reward = (increase/self.power_greedy_farm)*100
            
#         info = {}
#         # The observationspace is WD, WS, TI:
#         #observation = np.array([self.wd_norm, self.ws_norm, self.TI_norm])
#         observation = np.concatenate( (self.wd_norm, self.ws_norm, self.TI_norm, self.yaw_current_norm), axis = None)
#         return observation, reward, done, info
    
#     def reset(self):
    

#         #np.round(A,decimals=1)
#         self.ws = np.array(7, dtype=np.float32)
#         self.wd = np.array(270, dtype=np.float32)
#         self.TI = np.array(0.07, dtype=np.float32)
#         self.yaw_current = np.zeros(9, dtype=np.float32)
        
#         self.ws_norm = (self.ws - self.ws_range_min)/(self.ws_range_max - self.ws_range_min)
#         self.wd_norm = (self.wd - self.wd_range_min)/(self.wd_range_max - self.wd_range_min)
#         self.TI_norm = (self.TI - self.ti_range_min)/(self.ti_range_max - self.ti_range_min)
#         self.yaw_current_norm = self.yaw_current/self.yaw_max   
        
#         self.fi.reinitialize(
#             layout=(self.layout_x, self.layout_y),
#             wind_directions=[self.wd],
#             turbulence_intensity= self.TI,
#             wind_speeds=[self.ws]
#             )
        
#         self.wd_last = copy.copy(self.wd)
        
#         #Calculate greedy power. Used for normalization
#         self.fi.calculate_wake()
#         self.power_greedy_farm = self.fi.get_farm_power()[0][0]
        
#         self.time = 0
#         done = False
#         observation = np.concatenate( (self.wd_norm, self.ws_norm, self.TI_norm, self.yaw_current_norm), axis = None)
#         return observation  # reward, done, info can't be included
    
#     def render(self, mode='human'):
#         pass
    
#     def close (self):
#         pass

#     def change_seed(self, seed):
#         self.seed = seed

# ################################################################################################
# ################################################################################################

# class CustomEnv4(gym.Env):
#     """
#     This is for stepwise changes in the wind conditions. Also the yaw is now part of the observation space.
#     The inputs are:
#     t_steps     = number of timesteps pr simulation
#     dist        = rotor diameters between the turbines
#     nx          = number of turbines along x axis
#     ny          = number of turbines along y axis
#     turb_type   = The type of turbine used for the environment
#     combination = The combination model
#     deflection  = The deflection model
#     turbulence  = The turbulence model
#     velocity    = The wake velocity model
#     VS_min      = minimum wind speed [m/s]
#     VS_max      = maximum wind speed [m/s]
#     TI_min      = minimum turbulence intensity
#     TI_max      = maximum turbulence intensity
#     wd_min      = minimum wind direction
#     wd_max      = maximum wind direction
#     yaw_max     = Is the maximum yaw offset allowed in degrees.
    
#     """
#     #Custom Environment that follows gym interface
#     metadata = {'render.modes': ['human']}

#     def __init__(self, t_steps = 100, dist = 5, nx = 3, ny = 3,
#                turb_type = 'nrel_5MW', combination = 'sosfs', deflection = 'gauss',
#                turbulence = 'crespo_hernandez', velocity = 'gauss',
#                WS_min = 4, WS_max = 20, TI_min = 0.01, TI_max = 0.15, wd_min = 270, wd_max = 360, 
#                yaw_max = 30, rho = 1.225, seed = 0):
#         super(CustomEnv4, self).__init__()
        
#         self.ws_range_min = 2
#         self.ws_range_max = 20

#         self.ti_range_min = 0.0
#         self.ti_range_max = 0.20
        
#         self.wd_range_min = 0
#         self.wd_range_max = 360
        
#         self.SEED = seed

#         self.t_max = t_steps   #The number of "simulations" pr episode.
#         #self.wind_speed_min = WS_min
#         #self.wind_speed_max = WS_max
#         #self.TI_min         = TI_min
#         #self.TI_max         = TI_max
#         #self.wd_min         = wd_min
#         #self.wd_max         = wd_max
#         self.n_turb         = nx * ny
#         self.yaw_max        = yaw_max
#         self.rho            = rho
                     
#         #Creates the base for the farm
#         fi = FlorisInterface("gch.yaml")   
        
#         #Turns it into a dictionary and then does the changes to the model
#         fi_dict = fi.floris.as_dict()
        
#         fi_dict["farm"]["turbine_type"] = [turb_type]
#         fi_dict["wake"]["model_strings"]["combination_model"] = combination
#         fi_dict["wake"]["model_strings"]["deflection_model"]  = deflection
#         fi_dict["wake"]["model_strings"]["turbulence_model"]  = turbulence
#         fi_dict["wake"]["model_strings"]["velocity_model"]    = velocity
#         fi_dict["flow_field"]["air_density"]                  = rho
        
#         # Turns it back into a floris object:
#         self.fi = FlorisInterface(fi_dict)

#         D = self.fi.floris.farm.rotor_diameters[0]

#         x = np.linspace(0, D*dist*nx, nx)
#         y = np.linspace(0, D*dist*ny, ny)

#         xv, yv = np.meshgrid(x, y, indexing='xy')
        
#         self.layout_x =  xv.flatten()
#         self.layout_y = yv.flatten()
        
        
#         # The actionspace is the 9 yaw angles.
#         self.action_space = spaces.Box(low=-1, high=1,
#                                             shape=(nx*ny,), dtype=np.float32)
        

#         self.observation_space = spaces.Box(low = -1, high = 1,
#                                             shape = (3 + nx*ny,), dtype=np.float32) #The observation space is now: [wd, ws, TI, yaw angles.]

#         random.seed(self.SEED)
#         np.random.seed(self.SEED)
#         self.reset()
        
#     def step(self, action):

#         if self.time >= self.t_max:
#             done =  True
#         else:
#             self.time += 1
#             done = False

#         # if 15 <= self.time <= 60:
#         #     print("Changing wind direction")

#         #     self.wd += 1
#         #     self.yaw_current += 1

        
#         self.wd_norm = 2 * (self.wd - self.wd_range_min)/(self.wd_range_max - self.wd_range_min) -1

        
#         self.fi.reinitialize(
#             layout=(self.layout_x, self.layout_y),
#             wind_directions=[self.wd],
#             turbulence_intensity= self.TI,
#             wind_speeds=[self.ws]
#             )
        
#         self.yaw_current += action 
#         self.yaw_current = np.clip(self.yaw_current, -self.yaw_max, self.yaw_max)
#         self.yaw_current_norm = 2 * (self.yaw_current + self.yaw_max)/(2*self.yaw_max) -1

#         if self.wd_last != self.wd:
#             #print("Now calculating new power")
#             #If wind direction has changed, then calculate a new power. 
#             #Calculate greedy power. Used for normalization
#             self.fi.calculate_wake()
#             self.power_greedy_farm = self.fi.get_farm_power()[0][0]

#         self.wd_last = copy.copy(self.wd)

#         self.fi.calculate_wake(yaw_angles=np.array([[self.yaw_current]]))  
        
#         self.power_agent_farm = self.fi.get_farm_power()[0][0]
        
#         #Calculates the pct increase in power!
#         #increase = self.power_agent_farm - self.power_greedy_farm
        
#         #reward = (increase/self.power_greedy_farm)*100
#         reward = self.power_agent_farm/self.power_greedy_farm -1

#         info = {"Current yaw angles": self.yaw_current,
#                 "Normalized yaw angles": self.yaw_current_norm,
#                 "Wind direction": self.wd
#                 }
#         # The observationspace is WD, WS, TI:
#         #observation = np.array([self.wd_norm, self.ws_norm, self.TI_norm])
#         observation = np.concatenate( (self.wd_norm, self.ws_norm, self.TI_norm, self.yaw_current_norm), axis = None)
#         return observation, reward, done, info
    
#     def reset(self):

#         #np.round(A,decimals=1)
#         self.ws = np.array(7, dtype=np.float32)
#         self.wd = np.array(270, dtype=np.float32)
#         self.TI = np.array(0.07, dtype=np.float32)
#         self.yaw_current = np.random.uniform(low = -self.yaw_max, high=self.yaw_max, size=self.n_turb).astype(np.float32)
#         #np.zeros(9, dtype=np.float32)
        
#         #scales it to be between -1 and 1.
#         self.ws_norm = 2 * (self.ws - self.ws_range_min)/(self.ws_range_max - self.ws_range_min) -1
#         self.wd_norm = 2 * (self.wd - self.wd_range_min)/(self.wd_range_max - self.wd_range_min) -1
#         self.TI_norm = 2 * (self.TI - self.ti_range_min)/(self.ti_range_max - self.ti_range_min) -1
#         self.yaw_current_norm = 2 * (self.yaw_current + self.yaw_max)/(2*self.yaw_max) -1   #It is + instead of -, as yaw_min is not defined.
        
#         self.fi.reinitialize(
#             layout=(self.layout_x, self.layout_y),
#             wind_directions=[self.wd],
#             turbulence_intensity= self.TI,
#             wind_speeds=[self.ws]
#             )
        
#         self.wd_last = copy.copy(self.wd)
        
#         #Calculate greedy power. Used for normalization
#         self.fi.calculate_wake()
#         self.power_greedy_farm = self.fi.get_farm_power()[0][0]
        
#         self.time = 0
#         done = False
#         observation = np.concatenate( (self.wd_norm, self.ws_norm, self.TI_norm, self.yaw_current_norm), axis = None)
#         #print(observation)
#         return observation  # reward, done, info can't be included
    
#     def render(self, mode='human'):
#         pass
    
#     def close (self):
#         pass

#     def change_seed(self, seed):
#         self.seed = seed

# ######################################################
# ################# ENV 5 ##############################
# ######################################################

class CustomEnv5(gym.Env):
    """
    This is for stepwise changes in the wind conditions. Also the yaw is now part of the observation space.
    The inputs are:
    t_steps     = number of timesteps pr simulation
    dist        = rotor diameters between the turbines
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

    def __init__(self, t_steps = 100, dist = 5, nx = 3, ny = 3,
               turb_type = 'nrel_5MW', combination = 'sosfs', deflection = 'gauss',
               turbulence = 'crespo_hernandez', velocity = 'gauss',
               WS_min = 4, WS_max = 20, TI_min = 0.01, TI_max = 0.15, wd_min = 270, wd_max = 360, 
               yaw_max = 30, rho = 1.225, seed = 0):
        super(CustomEnv5, self).__init__()
        
        self.ws_range_min = 2
        self.ws_range_max = 20

        self.ti_range_min = 0.0
        self.ti_range_max = 0.20
        
        self.wd_range_min = 0
        self.wd_range_max = 360
        
        self.SEED = seed

        self.t_max = t_steps   #The number of "simulations" pr episode.
        #self.wind_speed_min = WS_min
        #self.wind_speed_max = WS_max
        #self.TI_min         = TI_min
        #self.TI_max         = TI_max
        #self.wd_min         = wd_min
        #self.wd_max         = wd_max
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
        

        self.observation_space = spaces.Box(low = -1, high = 1,
                                            shape = (3,), dtype=np.float32) #The observation space is now: [wd, ws, TI]

        random.seed(self.SEED)
        np.random.seed(self.SEED)
        self.reset()
        
    def step(self, action):

        if self.time >= self.t_max:
            done =  True
        else:
            self.time += 1
            done = False
        
        self.fi.reinitialize(
            layout=(self.layout_x, self.layout_y),
            wind_directions=[self.wd],
            turbulence_intensity= self.TI,
            wind_speeds=[self.ws]
            )
        
        self.yaw_current = action * self.yaw_max 
        self.yaw_current_norm = action


        self.fi.calculate_wake()
        self.power_greedy_farm = self.fi.get_farm_power()[0][0]


        self.fi.calculate_wake(yaw_angles=np.array([[self.yaw_current]]))  
        
        self.power_agent_farm = self.fi.get_farm_power()[0][0]
        
        #Calculates the pct increase in power!
        #increase = self.power_agent_farm - self.power_greedy_farm
        
        #reward = (increase/self.power_greedy_farm)*100
        reward = self.power_agent_farm/self.power_greedy_farm - 1

        info = {"Current yaw angles": self.yaw_current,
                "Normalized yaw angles": self.yaw_current_norm,
                "Wind direction": self.wd
                }
        # The observationspace is WD, WS, TI:
        #observation = np.array([self.wd_norm, self.ws_norm, self.TI_norm])
        #observation = np.concatenate( (self.wd_norm, self.ws_norm, self.TI_norm), axis = None).astype(np.float32)
        return self.observation, reward, done, info
    
    def reset(self):

        #np.round(A,decimals=1)
        self.ws = np.array(7, dtype=np.float32)
        self.wd = np.random.choice((270, 275, 280, 285, 290, 295, 300, 305, 310, 315)).astype(np.float32)
        self.TI = np.array(0.07, dtype=np.float32)
        self.yaw_current = np.random.uniform(low = -self.yaw_max, high=self.yaw_max, size=self.n_turb).astype(np.float32)
        #np.zeros(9, dtype=np.float32)
        
        #scales it to be between -1 and 1.
        # self.ws_norm = 2 * (self.ws - self.ws_range_min)/(self.ws_range_max - self.ws_range_min) -1
        # self.wd_norm = 2 * (self.wd - self.wd_range_min)/(self.wd_range_max - self.wd_range_min) -1
        # self.TI_norm = 2 * (self.TI - self.ti_range_min)/(self.ti_range_max - self.ti_range_min) -1
        # self.yaw_current_norm = 2 * (self.yaw_current + self.yaw_max)/(2*self.yaw_max) -1   #It is + instead of -, as yaw_min is not defined.

        obs_scaled = self.scale_obs(self.ws, self.wd, self.TI)
        
        self.fi.reinitialize(
            layout=(self.layout_x, self.layout_y),
            wind_directions=[self.wd],
            turbulence_intensity= self.TI,
            wind_speeds=[self.ws]
            )
        
        #self.wd_last = copy.copy(self.wd)
        
        #Calculate greedy power. Used for normalization
        self.fi.calculate_wake()
        self.power_greedy_farm = self.fi.get_farm_power()[0][0]
        
        self.time = 0
        done = False
        self.observation = obs_scaled
        #print(observation)
        return self.observation  # reward, done, info can't be included

    def scale_obs(self, ws, wd, TI):
        #Takes inputs and scales them to fit the observation space.

        self.ws_norm = 2 * (ws - self.ws_range_min)/(self.ws_range_max - self.ws_range_min) -1
        self.wd_norm = 2 * (wd - self.wd_range_min)/(self.wd_range_max - self.wd_range_min) -1
        self.TI_norm = 2 * (TI - self.ti_range_min)/(self.ti_range_max - self.ti_range_min) -1  

        obs_scaled = np.concatenate( (self.wd_norm, self.ws_norm, self.TI_norm), axis = None).astype(np.float32)
        return obs_scaled
    
    def render(self, mode='human'):
        pass
    
    def close (self):
        pass

    def change_seed(self, seed):
        self.seed = seed



# ######################################################
# ################# ENV 6 ##############################
# ######################################################

class CustomEnv6(gym.Env):
    """
    This is for stepwise changes in the wind conditions. Also the yaw is now part of the observation space.
    The inputs are:
    t_steps     = number of timesteps pr simulation
    dist        = rotor diameters between the turbines
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

    def __init__(self, t_steps = 100, dist = 5, nx = 3, ny = 3,
               turb_type = 'nrel_5MW', combination = 'sosfs', deflection = 'gauss',
               turbulence = 'crespo_hernandez', velocity = 'gauss',
               WS_min = 4, WS_max = 20, TI_min = 0.01, TI_max = 0.15, wd_min = 270, wd_max = 360, 
               yaw_max = 30, rho = 1.225, seed = 0):
        super(CustomEnv6, self).__init__()
        
        self.ws_range_min = 2
        self.ws_range_max = 20

        self.ti_range_min = 0.0
        self.ti_range_max = 0.20
        
        self.wd_range_min = 0
        self.wd_range_max = 360
        
        self.SEED = seed

        self.t_max = t_steps   #The number of "simulations" pr episode.
        #self.wind_speed_min = WS_min
        #self.wind_speed_max = WS_max
        #self.TI_min         = TI_min
        #self.TI_max         = TI_max
        #self.wd_min         = wd_min
        #self.wd_max         = wd_max
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
        

        self.observation_space = spaces.Box(low = -1, high = 1,
                                            shape = (3,), dtype=np.float32) #The observation space is now: [wd, ws, TI]

        random.seed(self.SEED)
        np.random.seed(self.SEED)
        self.reset()
        
    def step(self, action):

        if self.time >= self.t_max:
            done =  True
        else:
            self.time += 1
            done = False

        
        self.fi.reinitialize(
            layout=(self.layout_x, self.layout_y),
            wind_directions=[self.wd],
            turbulence_intensity= self.TI,
            wind_speeds=[self.ws]
            )
        
        self.yaw_current = action * self.yaw_max 
        self.yaw_current_norm = action


        self.fi.calculate_wake()
        self.power_greedy_farm = self.fi.get_farm_power()[0][0]


        self.fi.calculate_wake(yaw_angles=np.array([[self.yaw_current]]))  
        
        self.power_agent_farm = self.fi.get_farm_power()[0][0]
        
        #Calculates the pct increase in power!
        #increase = self.power_agent_farm - self.power_greedy_farm
        
        #reward = (increase/self.power_greedy_farm)*100
        reward = self.power_agent_farm/self.power_greedy_farm -1

        self.wd = np.random.choice((270, 315)).astype(np.float32)
        self.wd_norm = 2 * (self.wd - self.wd_range_min)/(self.wd_range_max - self.wd_range_min) -1

        info = {"Current yaw angles": self.yaw_current,
                "Normalized yaw angles": self.yaw_current_norm,
                "Wind direction": self.wd
                }
        # The observationspace is WD, WS, TI:
        #observation = np.array([self.wd_norm, self.ws_norm, self.TI_norm])
        observation = np.concatenate( (self.wd_norm, self.ws_norm, self.TI_norm), axis = None).astype(np.float32)
        return observation, reward, done, info
    
    def reset(self):

        #np.round(A,decimals=1)
        self.ws = np.array(7, dtype=np.float32)
        self.wd = np.random.choice((270, 315)).astype(np.float32)
        self.TI = np.array(0.07, dtype=np.float32)
        self.yaw_current = np.random.uniform(low = -self.yaw_max, high=self.yaw_max, size=self.n_turb).astype(np.float32)
        #np.zeros(9, dtype=np.float32)
        
        #scales it to be between -1 and 1.
        self.ws_norm = 2 * (self.ws - self.ws_range_min)/(self.ws_range_max - self.ws_range_min) -1
        self.wd_norm = 2 * (self.wd - self.wd_range_min)/(self.wd_range_max - self.wd_range_min) -1
        self.TI_norm = 2 * (self.TI - self.ti_range_min)/(self.ti_range_max - self.ti_range_min) -1
        self.yaw_current_norm = 2 * (self.yaw_current + self.yaw_max)/(2*self.yaw_max) -1   #It is + instead of -, as yaw_min is not defined.
        
        self.fi.reinitialize(
            layout=(self.layout_x, self.layout_y),
            wind_directions=[self.wd],
            turbulence_intensity= self.TI,
            wind_speeds=[self.ws]
            )
        
        self.wd_last = copy.copy(self.wd)
        
        #Calculate greedy power. Used for normalization
        self.fi.calculate_wake()
        self.power_greedy_farm = self.fi.get_farm_power()[0][0]
        
        self.time = 0
        done = False
        observation = np.concatenate( (self.wd_norm, self.ws_norm, self.TI_norm), axis = None).astype(np.float32)
        #print(observation)
        return observation  # reward, done, info can't be included
    
    def render(self, mode='human'):
        pass
    
    def close (self):
        pass

    def change_seed(self, seed):
        self.seed = seed

#########################################################################
########################### ENV 7 #######################################
#########################################################################

class CustomEnv7(gym.Env):
    """
    t_steps     = number of timesteps pr simulation
    dist        = rotor diameters between the turbines
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

    def __init__(self, t_steps = 100, dist = 5, nx = 3, ny = 3,
               turb_type = 'nrel_5MW', combination = 'sosfs', deflection = 'gauss',
               turbulence = 'crespo_hernandez', velocity = 'gauss',
               WS_min = 4, WS_max = 20, TI_min = 0.01, TI_max = 0.15, wd_min = 270, wd_max = 360, 
               yaw_max = 30, rho = 1.225, seed = 0):
        super(CustomEnv7, self).__init__()
        
        self.ws_range_min = 2
        self.ws_range_max = 20

        self.ti_range_min = 0.0
        self.ti_range_max = 0.20
        
        self.wd_range_min = 0
        self.wd_range_max = 360
        
        self.SEED = seed

        self.t_max = t_steps   #The number of "simulations" pr episode.
        #self.wind_speed_min = WS_min
        #self.wind_speed_max = WS_max
        #self.TI_min         = TI_min
        #self.TI_max         = TI_max
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
        

        self.observation_space = spaces.Box(low = -1, high = 1,
                                            shape = (3,), dtype=np.float32) #The observation space is now: [wd, ws, TI]

        random.seed(self.SEED)
        np.random.seed(self.SEED)
        self.reset()
        
    def step(self, action):

        if self.wd > self.wd_max:
            done =  True
        else:
            done = False
        
        self.fi.reinitialize(
            layout=(self.layout_x, self.layout_y),
            wind_directions=[self.wd],
            turbulence_intensity= self.TI,
            wind_speeds=[self.ws]
            )
        
        self.yaw_current = action * self.yaw_max 

        self.fi.calculate_wake()
        self.power_greedy_farm = self.fi.get_farm_power()[0][0]


        self.fi.calculate_wake(yaw_angles=np.array([[self.yaw_current]]))  
        self.power_agent_farm = self.fi.get_farm_power()[0][0]
        
        #Calculates the pct increase in power!
        #increase = self.power_agent_farm - self.power_greedy_farm
        
        #reward = (increase/self.power_greedy_farm)*100
        reward = self.power_agent_farm/self.power_greedy_farm - 1

        # If negative reward, add large penalty.
        if reward < 0:
            reward += -3

        self.wd += 0.5

        obs_scaled = self.scale_obs(self.wd, self.ws, self.TI)
        self.observation = obs_scaled



        info = {}
        # The observationspace is WD, WS, TI:
        return self.observation, reward, done, info
    
    def reset(self):

        #np.round(A,decimals=1)
        self.ws = np.array(7, dtype=np.float32)
        #self.wd = np.random.choice((270, 275, 280, 285, 290, 295, 300, 305, 310, 315)).astype(np.float32)
        self.wd = self.wd_min
        self.TI = np.array(0.07, dtype=np.float32)

        obs_scaled = self.scale_obs(self.wd, self.ws, self.TI)
        
        self.fi.reinitialize(
            layout=(self.layout_x, self.layout_y),
            wind_directions=[self.wd],
            turbulence_intensity= self.TI,
            wind_speeds=[self.ws]
            )
        
        
        #Calculate greedy power. Used for normalization
        self.fi.calculate_wake()
        self.power_greedy_farm = self.fi.get_farm_power()[0][0]
        
        self.time = 0
        done = False
        self.observation = obs_scaled
        return self.observation  # reward, done, info can't be included

    def scale_obs(self, wd, ws, TI):
        #Takes inputs and scales them to fit the observation space.

        self.ws_norm = 2 * (ws - self.ws_range_min)/(self.ws_range_max - self.ws_range_min) -1
        self.wd_norm = 2 * (wd - self.wd_range_min)/(self.wd_range_max - self.wd_range_min) -1
        self.TI_norm = 2 * (TI - self.ti_range_min)/(self.ti_range_max - self.ti_range_min) -1  

        obs_scaled = np.concatenate( (self.wd_norm, self.ws_norm, self.TI_norm), axis = None).astype(np.float32)
        return obs_scaled
    
    def render(self, mode='human'):
        pass
    
    def close (self):
        pass

    def change_seed(self, seed):
        self.seed = seed
