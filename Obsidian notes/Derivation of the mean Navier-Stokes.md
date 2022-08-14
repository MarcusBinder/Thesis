Here we are going to derive this expression:
$$
\partial_t \langle u_i \rangle + \langle u_j \rangle \partial_j \langle u_i \rangle = - \dfrac{1}{\rho} \partial_i \langle p \rangle + \nu \partial_j \partial_j \langle u_i \rangle - \partial_j \langle u_i' u_j' \rangle 
$$

We start by the original [[Navier-Stokes equation]]:
$$
\partial_t u_i + u_j\partial_j u_i = -\dfrac{1}{\rho} \partial_ip+\nu \partial_j \partial_ju_i
$$
Then taking the mean of it all:

$$
\langle \partial_t u_i + u_j\partial_j u_i = -\dfrac{1}{\rho} \partial_ip+\nu \partial_j \partial_ju_i \rangle
$$
The mean is ofcouse a linear operator, so we end up writing:

$$
\langle \partial_t u_i  \rangle + \langle  u_j\partial_j u_i \rangle =\langle -\dfrac{1}{\rho} \partial_ip \rangle+ \langle\nu \partial_j \partial_ju_i \rangle
$$

To make it easier to follow, I will write the individual steps for each term here:

**Term I**
$$
\langle \partial_t u_i  \rangle 
$$
We can't take the mean of the derivative term, so this just becomes:
$$
\langle \partial_t u_i  \rangle =  \partial_t \langle u_i  \rangle 
$$

**Term II**
$$
\langle  u_j\partial_j u_i \rangle
$$
This is the trouble term!  
We start by moving the partial to the left, and get:

$$
\partial_j \langle  u_j u_i \rangle
$$
We then use the definition of the fluctuations:
$$u = \langle u \rangle + u'
$$
This gives:

$$
\partial_j \langle  (\langle u_i \rangle + u_i') \cdot (\langle u_j \rangle + u_j') \rangle
$$
We can then expand the product, to get:

$$
\partial_j \langle  (\langle u_i \rangle \cdot \langle u_j \rangle + \langle u_i \rangle \cdot u_j' + u_i' \cdot \langle u_j \rangle + u_i'\cdot u_j') \rangle
$$
Now we have 4 terms. We can distribute the angle bracket, to get:


$$
\partial_j [  (\langle \langle u_i \rangle \cdot \langle u_j \rangle \rangle + \langle\langle u_i \rangle \cdot u_j' \rangle + \langle u_i' \cdot \langle u_j \rangle \rangle +  \langle u_i'\cdot u_j'\rangle) ]
$$
This gives:

$$
\langle \langle u_i \rangle \cdot \langle u_j \rangle \rangle = \langle  u_i \rangle \cdot \langle u_j \rangle 
$$
$$ \langle\langle u_i \rangle \cdot u_j' \rangle =  \langle u_i \rangle \cdot \langle u_j' \rangle = 0 \text{ Because } \langle u_j' \rangle=0
$$
$$
 \langle u_i' \cdot \langle u_j \rangle \rangle = \langle u_i' \rangle  \cdot \langle u_j \rangle = 0 \text{ Because } \langle u_i' \rangle = 0
$$
$$
\langle u_i'\cdot u_j'\rangle \text{ This term survives}
$$
This term is then:
$$
\partial_j (\langle u_i \rangle \langle u_j \rangle) + \partial_j \langle u_i' u_j' \rangle
$$
Note that he also rewrites it to be:

$$
\langle u_j \rangle \partial_j \langle u_i \rangle  + \partial_j \langle u_i' u_j' \rangle
$$

**Term III**
$$ \langle -\dfrac{1}{\rho} \partial_ip \rangle 
$$
Easy term, just gives:

$$  -\dfrac{1}{\rho} \partial_i \langle p \rangle 
$$

**Term IV**
$$\langle\nu \partial_j \partial_ju_i \rangle
$$
Also easy:
$$\nu \partial_j \partial_j \langle u_i \rangle
$$

The **Final** Reynolds equation then becomes:

$$
\partial_t \langle u_i  \rangle + \langle u_j \rangle \partial_j \langle u_i \rangle  =-\dfrac{1}{\rho} \partial_i \langle p \rangle + \nu \partial_j \partial_j \langle u_i \rangle - \partial_j \langle u_i' u_j' \rangle 
$$
Note that we have split up **Term II**

$\partial_j \langle u_i' u_j' \rangle$ this is the troble term as this is the nonlinear term... ):