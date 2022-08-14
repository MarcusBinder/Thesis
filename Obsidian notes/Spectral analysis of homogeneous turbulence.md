## Spectral analysis of homogenous turbulence

So this is some weird shit.

The point of this is to create an energy spectrum. Transform time series to Fourier series. Described using wavenumber. Contains a real and imaginary part which is the specific energy.

Here we can see a function transformed using Fourier analysis.
![[Pasted image 20220523184933.png]]


### 1D Fourier transform
$$
\hat{u}(k) = \dfrac{1}{2 \pi} \int u(x)e^{-ikx}dx
$$
Note that k is the wavenumber here.
### **inverse Fourier transform**
$$
u(x) =  \int \hat{u}(k)e^{ikx}dk
$$
That was for continuous functions. If we had discrete it would look like:
### Discrete Fourier transforms

$$
\bar{u}(k) = \dfrac{1}{N}\sum_{j=0}^{N} u_j e^{-ikj} 
$$

$$
u(x=x_j) =\sum_{k=-N/2}^{N/2-1} \hat{u}_k e^{ikx_j} 
$$

Also if we were so inclined as to do some differentiation, then we would need:

$$
\dfrac{du}{dx}(x=x_j) =\sum_{k=-N/2}^{N/2-1} ik\hat{u}_k e^{ikx_j} 
$$
$$
\dfrac{d^2u}{dx^2}(x=x_j) =\sum_{k=-N/2}^{N/2-1} -k^2\hat{u}_k e^{ikx_j} 
$$
### Energy spectrum
Now for what we have all been waiting for!
We just learned how to take the discrete Fourier transform...
Well we can get something called the energy spectrum by:
**Energy spectrum 1D**:
$$
|\hat{u}(k)|^2 = |\hat{u}_{real,part}(k)|^2 + |\hat{u}_{imag,part}(k)|^2
$$
Also note that we only use the fluctuations. That means that $u = u'$.
We can then write:
$$
\sigma_u^2 = \langle u^2 \rangle = \int_0 ^\infty E_{11}(k) dk
$$
Where:
$$
E_{11}(k) = \langle \hat{u}(k) \hat{u}^*(k) \rangle = |\hat{u}(k)|^2
$$
Note that the * denotes that it's the [[complex conjugate]]...
All of this says that if we sum up all the energy spectrums, we end up with the standard deviation of the flow.

Also if it were **discrete**:
$$
\sigma_u^2 = \langle u^2 \rangle = \dfrac{1}{N} \sum_{j=0}^{N} u_j^2 =\sum_{k=-N/2}^{N/2-1} E_{11}(k)
$$

Also note that
$E_{11}(k=0)=\langle u \rangle$ which is 0, as u=u'

## Spectrum of isotropic turbulence
So we can plot the E from the energy spectrum as a function of the wavenumber k.
It describes the energy content of the eddies at different sizes.
![[Pasted image 20220524131648.png]]
There is also this picture:
![[Pasted image 20220524131703.png]]

![[Pasted image 20220524131737.png]]

**Take aways:**
- Larger reynolds number, the smaller kolmogoroc scale becomes, and the k (wave number) becomes larger
- The energy contraining range, and the dissipation range reaim the same size, but where it begins shifts.
- The middle size turbulent eddies ’feel’ neither the effects of viscosity, nor the generation of TKE. Their size is determined uniquely by $\epsilon$ 