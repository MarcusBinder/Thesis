# Adding axial induction to Floris

This is a document to try and contain what I have learnt. 

To keep it simple, im testing with the jensen wake model.

The Floris->simulation->wake_velocity->Jensen is what i tried changing.

The fi.calculate_wake() at some point calls the jensen.py file.

The jensen.py calculates the velocity deficit. $\dfrac{\Delta U}{U_\infty}$ 

It takes the axial induction as a input to the function. If I tried changing it inside the function by overwriting it, the following happende.
If I set a up, the power output fell, as this makes the velocity deficit larger.

If a was lowered, then the power output rose, as this makes the velocity deficit smaller.
_______________
So the calculate_wake() function works by calling the floris.steady_state_atmospheric_condition() function.
This then calls a solver, depending on what velocity model is being used. 
It distinguishes between cc, turbopark and then all the rest are being taken care of in the sequential_solver() function. 

The sequential solver function is being run from line 48-211. 
This works by having a for loop that calculates the velocity deficit sequentially from upstream to downstream turbines.
In this for loop, it does some sorting, and then it calculates the CT first, in the Ct() function.
After that it calls the axial_induction() function. 

My plan is to put in a scaling value for this Ct function, that, like the yaw angles, makes it possible to scale the Ct from 0-1. 

The plan is to recreate something like the yaw angles, but with a scaling factor. 

farm.yaw_angles_sorted


## What has been done:
So floris works somewhat like this:

First we use **fi.reinitialize**, to create the turbines, and set up all the vectors/matrices used for the calculations... I have not edited this function.

All the good stuff, happens inside the **fi.calculate_wake()** function. This takes a vector with the yaw angles for all the turbines, but i have edited it so it now also takes a "scaling factor" for each turbine. 

Inside calculate wake, it does 2 things.
1) **initialize_domain()**. This function first initializes the velocity field, and then it uses **farm.initialize**, to sort the yaw angles, so the ones that are upsteam comes first in the yaw.angles_sorted.... I added a self.scaling_sorted() that does the same, just with the scaling parameters.
2) **steady_state_atmospheric_condition()** This function choses what solver to use, depending on what velocity model is used. It has:
	1) 'cc' this is the cumulative gauss curl model. If this is the velocity model, then it uses the cc_solver()
	2) 'turboparl'. This is the turbopark velocity model. If this is used, then it uses the turbopark_solver
	3) For the rest (Jensen and gauss) it uses the sequential solver.
I have edited the cc solver and the sequential solver to take this scaling factor into account.
Both solvers loops over all the turbines and then calculates a velocity deficit, and also the vake curl and added turbulence. 
I edited the Ct function, so it now works the same as before, but it gets multiplied with a scaling factor between 0-1 before it gets returned.

The axial induction function is also slightly modified, as this value is calculated depending on the Ct value. I updated the call to the Ct() inside the axial induction function to now use the new Ct funciton.  
$$ a = \dfrac{0.5}{cos(yaw)} \cdot (1-\sqrt{1-Ct \cdot cos(yaw) } $$
So this new Ct value changes the axial induction aswell. 

The Ct and the axial induction is then used throughout the rest of the program to calculate velocity deficits, wake curls, added turbulence. 

I have done the same for the cc_solver, so that the Ct() and axial_induction() functions have been updated. 

This of course only updates the velocity field for the turbines. The power output needs to be updated aswell.
The power is calculated by the **fi.get_turbine_powers()** function, that calls the **power()** function. This has been updated, to now also take an scaling factor into it. 
The power is calculated like this is floris:
First the velocity the turbines experience, is calculated to a *yaw_effective_velocity*. This is done by:
$$ \text{yaw effective velocity} =  \left( \dfrac{\rho}{1.225} \right) ^{1/3} \cdot U_{averge} \cdot cos(yaw)^{p_P/3} $$
This velocity is then used by the power interpreter, to calculate the power output of the turbine. It does this by linear interpolation, the windspeed to a power output. 
After this is done, I have added the scaling factor to the p, and then it gets multiplied with 1.225 and returned.
The 1.225 stems from here: https://github.com/NREL/floris/issues/211
Also for more explanations about the power formula, look here: https://github.com/NREL/floris/discussions/417 

__________
# Full flow

So now the calculate_wake() function works allright, but the plots are broken!
