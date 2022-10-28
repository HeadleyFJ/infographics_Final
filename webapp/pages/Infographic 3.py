import streamlit as st
"This is the gravity simulation infographic"

import numpy as np
import matplotlib.pyplot as plt

# %matplotlib inline

# variable definitions are in SI units
G = 6.67*(10**-11)
M_Earth = 6*(10**24)
r_Earth = 6.4*(10**6)

# conditions on the radius of the large body and the initial starting position
M_planet = 1.5*M_Earth
r_planet = 1.5*r_Earth
s_initial_vertical = (1.5*r_planet)/r_Earth

# these definitions are for the graph to plot out the shape of the exoplanet
theta = np.arange(0, ((np.pi/2)+(np.pi/360)), np.pi/360)
# the Earth radius below is the ratio of the radius of Earth compared to itself
# and the planet radius is a ratio of the exoplanet's and Earth's radii
Earth_radius = 1. + (0*theta)
planet_radius = (r_planet/r_Earth) + (0*theta)

# initial conditions for the plot
u = [0, 0]
a = [0, -(G*M_planet)/(r_planet*r_planet)]
s_Earth = s_initial_vertical + u[1]*theta + 0.5*a[1]*theta*theta
s_planet = s_initial_vertical + u[1]*theta + 0.5*a[1]*theta*theta

# line 1 on the plot, ends on the surface of Earth
index = 0
for position in s_Earth:
  if position < Earth_radius[0]:
    s_Earth[index] = Earth_radius[0]
  index = index + 1

# line 2 on the plot, ends of the surface of the specified planet
index = 0
for position in s_planet:
  if position < planet_radius[0]:
    s_planet[index] = planet_radius[0]
  index = index + 1

fig = plt.figure(figsize=(10,8))
polar_ax = fig.add_subplot(1, 1, 1, projection="polar")
polar_ax.set_theta_zero_location('N')
polar_ax.set_theta_direction(-1)
polar_ax.set_ylim((0*s_initial_vertical), (1.1*s_initial_vertical))
polar_ax.set_xlim(0, (np.pi/2))
plt.plot(theta, s_Earth, color='black', zorder=5)
plt.plot(theta, s_planet, color='black', zorder=6)
plt.plot(theta, planet_radius, color='orange',zorder=3)
plt.fill_between(theta, planet_radius, alpha=0.5, color='orange', label='Radius of Exoplanet', zorder=2)
plt.plot(theta, Earth_radius, color='red',zorder=4)
plt.fill_between(theta, Earth_radius, alpha=0.5, color='red', label='Radius of Earth',zorder=1)
# plt.yticklabels('')
polar_ax.yaxis.grid(False)
polar_ax.xaxis.grid(False)
plt.ylabel("Radius (as a ratio of the Earth's radius)")
# polar_ax.xaxis('off')
polar_ax.axes.get_xaxis().set_visible(False)
polar_ax.legend(loc=0)

st.pyplot(fig=None, clear_figure=None)
st.set_option('deprecation.showPyplotGlobalUse', False)
