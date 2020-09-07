import matplotlib.pyplot as plt
import numpy as np
from numpy.random import randint

%matplotlib inline

x = np.linspace(0, 10, 20)
x


y = randint(1, 50, 20)
y

y.size

dir(plt)

plt.plot(y)

fig,ax = plt.subplots(1, 2)
y2 = x*y
col = ['r', 'g']
data = [y, y2]


for i, axes in enumerate(ax):
    axes.plot(x, data[i], col[i])
    
fig.tight_layout()

fig, ax = plt.subplots(figsize = (8,4), dpi = 100)

ax.plot(x, y, 'b', label = 'y')
ax.plot(x, y2, 'r', label = 'y*x')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('ramdom number plot')
ax.legend()

fig, ax = plt.subplots()
ax.plot(x, y, 'b2--', markersize = 12, linewidth = 3)

x = ('1', '14', '6', '1', '0', '2', '6', '2', '1', '4', '1', '0', '5')
x

plt.plot(x)

y = ('1', '14', '6', '1', '0', '2', '6', '2', '1', '4', '1', '0', '5')
plt.plot(y)

plt.scatter(x, y)





data = ('1', '14', '6', '1', '0', '2', '6', '2', '1', '4', '1', '0', '5')

data

plt.bar(data, height=1)



plt.hist(data, rwidth=0.8)







