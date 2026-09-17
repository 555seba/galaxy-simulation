import numpy as np

r = np.random.exponential(5,500)
angle = r * 0.5 + np.random.normal(0,0.15,500)

brightness = np.random.uniform(0.2, 1.0, 500)
brightness2 = np.random.uniform(0.2, 1.0, 500)

center_r = np.random.exponential(0.7,1000)
center_angle = np.random.uniform(0,2 * np.pi, 1000)

x = r * np.cos(angle)
y = r * np.sin(angle)
z = np.random.normal(0, 0.15, 500)

#print(x)
#print(y)

x2 = r * np.cos(angle + np.pi)
y2 = r * np.sin(angle + np.pi)
z2 = np.random.normal(0, 0.15, 500)

#print(x2)
#print(y2)

center_x = center_r * np.cos(center_angle)
center_y = center_r * np.sin(center_angle)
center_z = np.random.normal(0, 0.15, 1000)

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111,projection="3d")
ax.scatter(x,y,z,s=2, alpha=brightness)
ax.scatter(x2,y2,z2,s=2, alpha=brightness2)
ax.view_init(elev=20, azim=45)
#ax.view_init(elev=90, azim=0)
ax.scatter(center_x, center_y, center_z, s=4, alpha=0.4)
ax.scatter(center_x, center_y, center_z, s=12, alpha=0.05)
plt.show()