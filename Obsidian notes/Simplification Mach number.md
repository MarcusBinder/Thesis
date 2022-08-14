# Simplification incompresibility

We are going to start with the conservation of momentum equation, written in this form:
$$
\dfrac{\partial}{\partial t}  \rho \textbf{V} + \nabla ( \rho \textbf{V}\textbf{V})= -\nabla p + \bar{\bar{\tau}} + \rho \textbf{g} 
$$
We know that p varies, and as the density is a function of the pressure (p) and the temperature (T) then  $\rho$ varies aswell.

So [[Pourya]] kinda made the argument that the first and 2 last terms in the equation doesn't really contribute, so we are gonna end up with this:
$$
 \nabla ( \rho \textbf{V}\textbf{V})= -\nabla p  
$$
If we are on a streamline we have the following:
![[Pasted image 20220201193113.png]]
$$
\rho v dv \approx -dp
$$
We also know the the formula for the speed of sound is:
$$
c = \sqrt{\dfrac{dp}{d\rho}} \\

$$

We can then write the following math.
We make use of the fact that $v/c=M$

$$
\begin{align*}
\rho v dv \approx -dp \\
\rho v dv \approx -dp \dfrac{d \rho}{d\rho} \\
\rho v dv \approx -c^2 d \rho  \\
\rho \dfrac{dv}{v}= - \dfrac{c^20}{v^2} d \rho \\
\rho \dfrac{dv}{v}= - \dfrac{1}{M^2} d \rho \\
M^2 \dfrac{dv}{v} = - \dfrac{d\rho}{\rho}

\end{align*}
$$
So we can see that if M is much smaller then 1, then the density is almost constant!


