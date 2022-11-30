title: Normal Distribution
Date: 2022-05-26 21:22
Authors: Alex



### Normal Distribution

There is a pymc library wich gives you access to all kind of distributions: <https://www.pymc.io/projects/docs/en/stable/api/distributions.html>.

Populations in nature tend to be of average measurement unit for a normally distributed attribute (weight, height etc) with ocasionally occuring exceptions. This attribute can take on any real number but the value is ofther close to average(mean).

If a distribution of values occillates around an average then it is normal distribution.
Normal distribution is of continuous type and is opposed to uniform distribution.
```python
import matplotlib.pyplot as plt
import numpy as np
import arviz as az
plt.style.use('arviz-darkgrid')
x = np.linspace(-3, 3, 500)
ls = [0., -2]
us = [2., 1]
for l, u in zip(ls, us):
    y = np.zeros(500)
    y[(x<u) & (x>l)] = 1.0/(u-l)
    plt.plot(x, y, label='lower = {}, upper = {}'.format(l, u))
plt.xlabel('x', fontsize=12)
plt.ylabel('f(x)', fontsize=12)
plt.ylim(0, 1)
plt.legend(loc=1)
plt.show()

```