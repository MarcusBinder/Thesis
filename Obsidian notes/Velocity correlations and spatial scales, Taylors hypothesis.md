# Spatial scales and velocity correlations

## Correlations
If something is correlated it has a "connection" to something. 

There are a couple of different correlations.
**2 point 2 time** velocity correlations
$$
R_{ij}(x,x',t,t')= \langle u_i'(x,t) u_j'(x',t') \rangle
$$
This is the correlation of 2 different points, but also at 2 different times.

**2 point** correlations
$$
R_{ij}(x,x',t)= \langle u_i'(x,t) u_j'(x',t) \rangle
$$
The time is now the same, but it's for 2 points in space.


If we have homogeneity, then $R_{ij}$ only depends on the difference between the x, and not the space.
$$
R_{ij}(r,t)= \langle u_i'(x+r,t) u_j'(x,t) \rangle
$$

Note that if $r=0$, we end up with the Reynolds stress.
$$
R_{ij}(r=0,t)= \langle u_i'(x+0,t) u_j'(x,t) \rangle = \langle u_i'(x,t) u_j'(x,t) \rangle  = \Sigma_{ij}(x,t)
$$
Note that $\Sigma_{ij}$ can be seen at a 1 point velocity correlation tensor.
This can also be connected to the turbulent kinetic energy ([[Mean flow equations, energetics of the total and mean flows#kinetic energies|TKE]]) as:
$$
k(x,t)=\dfrac{1}{2}R_{ii}(r=0,t)
$$

### Properties of correlations
If we are in a **total random system** then we have no correlation
$$
R_{ij}(r,t) = 0
$$
If we have infinite distance, then there is zero correlation
$$
R_{ij}(r,t) = 0 \text{ when } |r| \rightarrow \infty 
$$
But we have maximum correlation is there is no distance

$$
R_{ij} = max \text{ when } r=0
$$

### Correlation coefficient
This is a "normalized" $R_{ij}$

$$
\rho_{ij} = \dfrac{R_{ij}(r,t)}{\tilde{u_i}(x,t)\tilde{u_j}(x,t)}
$$
Where $\tilde{u} = \langle u'^2 \rangle ^{1/2}$  is the rms of u'.

Note that the autocorrelation for noice is zero as there is no correlation in it!
## Integral length scale
So for some fucking reason we can calculate the longitudinal integral lengthscale from $\rho_{11}$

$$
L(t) = \int_0 ^\infty \rho_{11}(r,t) dr
$$
$L$ is a correlation scale. It's a measurable quantity, connected to the largest eddies of the turbulence.
$$
L \sim l_0
$$

the $l_0$ is from: [[Space and time scales of turbulence, energy cascades, kolmogorov hypothesis#Kolmogorov hypothesis|Kolmogorov hypothesis]].
$L$ is a measure of the energy-containing range, where the energy starts the [[Space and time scales of turbulence, energy cascades, kolmogorov hypothesis#Energy cascade|energy cascade]].

## Integral time scale

You can also use autocorrelation to do the integral time scale.

$$
t_1 = \int_0 ^\infty \rho(\tau) d\tau
$$


## Taylors hypothesis

Taylors hypothesis (also called the **frozen flow hypothesis**), states that we can make a temporal measurement to a spatial measurements.

He said that for any variable $\xi$, if the total derivative D/dt = 0, then the flow is "frozen"
$$
D_t \xi = \partial_t \xi + u\partial_x \xi+ v \partial_y \xi +  w\partial_z \xi = 0 $$

If the flow is only in the x direction we have that:
$$
\partial_t \xi = - \langle u \rangle \partial_x \xi
$$
*It says that the time derivative of a function is the negative mean value multiplied with space derivative*
Using this, we can use the autocorrelation for a time, to estimate the spatial integral scale.

$$
dt = -\langle u \rangle dx
$$
**This can then be used to  estimate the spatial integral scale:**
$$
L_I = \langle u \rangle t_I
$$
The Taylor’s (frozen flow) hypothesis can only be used when the turbulent eddies evolve with a
time scale much longer than the time it takes the eddies to get advected past the sensor (blive
ført forbi sensoren).

The eddies are evolving so slow that the time it takes for them to pass the sensor is nothing in comparison.  

The criterion before you can use the **frozen flow hypothesis** is that:
$$
\sigma_u \ll \langle u \rangle
$$
Where $\sigma_u$ is the RMS of $u'$.

We sometimes say that $\ll \langle u \rangle \text{ is } 0.5 \langle u \rangle$.

