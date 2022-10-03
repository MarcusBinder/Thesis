import numpy as np
from floris.tools import FlorisInterface
import matplotlib.pyplot as plt


fi = FlorisInterface("floris_examples/inputs/gch.yaml")


x_2x2 = [0, 0, 800, 800]
y_2x2 = [0, 400, 0, 400]

print("reinitialize first")
fi.reinitialize( layout=(x_2x2, y_2x2) )

print("reinitialize again")
fi.reinitialize( wind_directions=[270.0], wind_speeds=[8.0] )

yaw_test = np.zeros((1,1,4))
#yaw_test[0,0,2] = 10

print("calculating wake")
fi.calculate_wake(yaw_angles=yaw_test)


print("calculating powers")
powers = fi.get_turbine_powers() / 1000.0  # calculated in Watts, so convert to kW
print("power is:", powers)