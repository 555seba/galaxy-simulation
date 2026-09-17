import numpy as np

r = np.random.exponential(5,500)
angle = r * 0.5 + np.pi
x = r * np.cos(angle)
y = r * np.sin(angle) * 0.3
print(x)
print(y)
x2 = r * np.cos(angle + np.pi)
y2 = r * np.sin(angle + np.pi)
print(x2)
print(y2)


import matplotlib.pyplot as plt
plt.scatter(x,y, s=2)
plt.scatter(x2,y2, s=2)
plt.show()