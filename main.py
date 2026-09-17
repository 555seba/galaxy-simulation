import numpy as np


#PHYSICS
trajectory = []
mass = np.random.uniform(0.5, 2.0, 500)
G = 1.0 #G-Force aka gravity, not real world.
galaxy_mass = 1000.0
velocity = np.array([0.0, np.sqrt(G*galaxy_mass / 5), 0.0])
particle_mass = 1.0
position = np.array([5.0, 0.0, 0.0])
for _ in range(1000):
    distance = np.linalg.norm(position)
    force = (G * galaxy_mass) / distance**2
    direction = -position / distance
    force_vector = force * direction
    acceleration = force_vector / particle_mass
    dt = 0.01 #Interval between calculations
    velocity = velocity + acceleration * dt #New velocity equals old velocity plus acceleration times interval
    position = position + velocity * dt #New position equals old position plus new velocity times interval
    trajectory.append(position.copy())
trajectory = np.array(trajectory)
trajectory_x = trajectory[:,0]
trajectory_y = trajectory[:,1]
trajectory_z = trajectory[:,2]

brightness = np.random.uniform(0.2, 1.0, 500)
brightness2 = np.random.uniform(0.2, 1.0, 500)

r = np.random.exponential(5,500)
angle = r * 0.5 + np.random.normal(0,0.15,500)


center_r = np.random.exponential(0.7,1000)
center_angle = np.random.uniform(0,2 * np.pi, 1000)

x = r * np.cos(angle)
y = r * np.sin(angle)
z = np.random.normal(0, 0.15, 500)

x2 = r * np.cos(angle + np.pi)
y2 = r * np.sin(angle + np.pi)
z2 = np.random.normal(0, 0.15, 500)

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
ax.plot(trajectory_x, trajectory_y, trajectory_z) #Able to see how it moved under the influence of gravity
plt.show()