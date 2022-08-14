# SWMAL


Her er en liste med arbejdsopgaver i forbindelse med O4 til SWMAL

1) [ ] def render()  få den til at plotte den relle rute, og ikke bare en lige streg.
	- Det er bare er nice plots!  https://medium.com/future-vision/google-maps-in-python-part-2-393f96196eaf   Karl-Emil også her!
2) Undersøg typer af agenter der kan bruges. Dette kunne være https://en.wikipedia.org/wiki/Reinforcement_learning Q-learning, SARSA, osv. 
3) [x] Pipeline for data til enviroment 
	 - [x] Få data fra "vores" til at passe med delivery.py. 
4) Find flere adresser som skal i CSV filen.
	- 50 totalt
		- Karl-Emil laver det her.
5)  Get lang long skal erstatte de tilfædigt genereret punkter i hans kode. 
6) Få det implementeret i den her kode istedet for: https://medium.com/unit8-machine-learning-publication/routing-traveling-salesmen-on-random-graphs-using-reinforcement-learning-in-pytorch-7378e4814980 
	- Mig 
7) Andet eksempel kode: https://medium.com/betacom/travelling-salesman-problem-with-reinforcement-learning-eac425be87aa 
	- Ali 



### Custom environment

```python
class ENVIROMENT(Env):
	def __init__(self):
		#Actions we can take, down, stay, up
		self.action_space = Discrete(3)
		#Temperature array
		self.observation_space = Box(lov=np.array([0], high=np.array([100])))
		#Set start temp
		self.state = 38 + random.randint(-3,3)
		#Set shower length
		self.shower_length = 60
		
	def step(self):
		#Apply action
		#action 0 = down, so we minus 1 from temperature
		#action 1 = stay, so 1-1 = 0
		#action 2 = up, so 2-1 = 1 deg up
		self.state += action -1
		#reduce shower length by 1 second
		self.shower_length -= 1

		#Calculate reward
		if self.state >= 37 and self.state <= 39:
			reward = 1
		else: 
			reward = -1

		#Check if shower is done
		if self.shower_length <=0:
			done = True
		else:
			done = False

		#Apply random noise
		self.state += random.randint(-1,1)
		#Set placeholder for info. Something that openAI gym requires!
		info = {}

		# return step information
		return self.state, reward, done, info
		
	def render(self):
		#Implement viz
		pass
		
	def reset(self):
		#Reset shower temps
		self.state = 38 + random.randint(-3,3)
		#Set shower length
		self.shower_length = 60
		return self.state
```

## Environment from delivery.py

```python
class DeliveryEnvironment(object):
    def __init__(self,n_stops = 10,max_box = 10,method = "distance",**kwargs):
	    # just does initialization 
        # Initialization
        self.adresses = addresses = load_addresses("addresses.csv")


        self.n_stops = np.size(self.addresses,0)


        self.action_space = self.n_stops
        self.observation_space = self.n_stops
        self.max_box = max_box
        self.stops = []
        self.method = method

        # Generate stops
        self._generate_stops()
        self._generate_q_values()
        self.render()

        # Initialize first point
        self.reset()


    def _generate_stops(self):
		# Generate geographical coordinates
		# This needs to be replaced with something like:

		geocodes = get_lat_lon(self.addresses)
		self.x = x_vores = np.array(geocodes['lon'])
		self.y = y_vores = np.array(geocodes['lat'])

		xy = np.column_stack([self.x,self.y])

		#xy = np.random.rand(self.n_stops,2)*self.max_box
        #self.x = xy[:,0]
        #self.y = xy[:,1]


    def _generate_q_values(self,box_size = 0.2):

        # Generate actual Q Values corresponding to time elapsed between two points
        if self.method in ["distance","traffic_box"]:
            xy = np.column_stack([self.x,self.y])
            self.q_stops = dist_mat(addresses)
        else:
            raise Exception("Method not recognized")
    

    def render(self,return_img = False):
	    #Just renders. I dont care atm.


    def reset(self):

        # Stops placeholder
        self.stops = []

        # Random first stop
        first_stop = np.random.randint(self.n_stops)
        self.stops.append(first_stop)

        return first_stop


    def step(self,destination):

        # Get current state
        state = self._get_state()
        new_state = destination

        # Get reward for such a move
        reward = self._get_reward(state,new_state)

        # Append new_state to stops
        self.stops.append(destination)
        done = len(self.stops) == self.n_stops

        return new_state,reward,done
    

    def _get_state(self):
        return self.stops[-1]


    def _get_xy(self,initial = False):
        state = self.stops[0] if initial else self._get_state()
        x = self.x[state]
        y = self.y[state]
        return x,y


    def _get_reward(self,state,new_state):
        base_reward = self.q_stops[state,new_state]

        if self.method == "distance":
            return base_reward

    @staticmethod
    def _calculate_point(x1,x2,y1,y2,x = None,y = None):

        if y1 == y2:
            return y1
        elif x1 == x2:
            return x1
        else:
            a = (y2-y1)/(x2-x1)
            b = y2 - a * x2

            if x is None:
                x = (y-b)/a
                return x
            elif y is None:
                y = a*x+b
                return y
            else:
                raise Exception("Provide x or y")


    def _is_in_box(self,x,y,box):
        # Get box coordinates
        x_left,x_right,y_bottom,y_top = box
        return x >= x_left and x <= x_right and y >= y_bottom and y <= y_top


    def _calculate_box_intersection(self,x1,x2,y1,y2,box):

        # Get box coordinates
        x_left,x_right,y_bottom,y_top = box

        # Intersections
        intersections = []

        # Top intersection
        i_top = self._calculate_point(x1,x2,y1,y2,y=y_top)
        if i_top > x_left and i_top < x_right:
            intersections.append((i_top,y_top))

        # Bottom intersection
        i_bottom = self._calculate_point(x1,x2,y1,y2,y=y_bottom)
        if i_bottom > x_left and i_bottom < x_right:
            intersections.append((i_bottom,y_bottom))

        # Left intersection
        i_left = self._calculate_point(x1,x2,y1,y2,x=x_left)
        if i_left > y_bottom and i_left < y_top:
            intersections.append((x_left,i_left))

        # Right intersection
        i_right = self._calculate_point(x1,x2,y1,y2,x=x_right)
        if i_right > y_bottom and i_right < y_top:
            intersections.append((x_right,i_right))

        return intersections

```



[[A2C]]