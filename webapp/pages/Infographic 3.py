import streamlit as st
"This is the gravity simulation infographic"

import numpy as np
import matplotlib.pyplot as plt
import math

# %matplotlib inline

# variable definitions are in SI units
G = 6.67*(10**-11)
M_Earth = 6*(10**24)
r_Earth = 6.4*(10**6)

# conditions on the radius of the large body and the initial starting position
M_planet = st.slider("Exoplanet Mass", min_value = 1.0, max_value = 25.0, step = 1.0)
M_planet = M_planet*M_Earth
r_planet = st.slider("Exoplanet Radius", min_value = 1.0, max_value = 5.0, step = 0.1)
r_planet = r_planet*r_Earth
s_initial_vertical = (1.5*r_planet)/r_Earth
# these definitions are for the graph to plot out the shape of the exoplanet
theta = np.arange(0, ((np.pi/2) + (np.pi/720)), np.pi/720)
theta_list = [angle for angle in theta]

# this angle will be pre-defined in the program
angle = np.pi/4
# this speed will be specified by the user
new_speed = st.selectbox(
  "Please select a speed for the projectile on the exoplanet"
  [10, 100, 1000])

# this angle will need to be set to between 0 and pi/2
new_angle = np.pi/3
# the initial horizontal and vertical speed of the projectile on Earth
u_Earth = [100.*math.cos(angle), 100.*math.sin(angle)]
# the initial horizontal and vertical speed of the projectile on the exoplanet
u_planet = [new_speed*math.cos(new_angle), new_speed*math.sin(new_angle)]

# the Earth radius below is the ratio of the radius of Earth compared to itself
# and the planet radius is a ratio of the exoplanet's and Earth's radii
Earth_radius = 1. + (0*theta)
planet_radius = (r_planet/r_Earth) + (0*theta)

# initial conditions for the plot
a_planet = [0, -(G*M_planet)/(r_planet*r_planet)]
a_Earth = [0, -(G*M_Earth)/(r_Earth*r_Earth)]

s_initial = [0, 0]

time = np.arange(0, 33, 0.01)

s_planet_horizontal = [s_initial[0] + u_planet[0]*t + 0.5*a_planet[0]*t*t for t in time]
s_planet_vertical = [s_initial[1] + u_planet[1]*t + 0.5*a_planet[1]*t*t for t in time]
s_Earth_horizontal = [s_initial[0] + u_Earth[0]*t + 0.5*a_Earth[0]*t*t for t in time]
s_Earth_vertical = [s_initial[1] + u_Earth[1]*t + 0.5*a_Earth[1]*t*t for t in time]

index = 0
for position in s_Earth_vertical:
  if position > 0:
    index = index + 1
  if position < 0:
    # print(index)
    break

bucket_location = 0.5*(s_Earth_horizontal[index]+s_Earth_horizontal[index+1])
# print(bucket_location)

fig = plt.figure(figsize=(20, 20))
polar_ax = plt.subplot(2, 1, 1, projection='polar')
polar_ax.set_theta_zero_location('N')
polar_ax.set_theta_direction(-1)
polar_ax.set_ylim((0*s_initial_vertical), (1.1*planet_radius[0]))
polar_ax.set_xlim(0, (np.pi/2))
# plt.plot(theta, s_Earth, color='black', zorder=5)
# plt.plot(theta, s_planet, color='black', zorder=6)
plt.plot(theta, planet_radius, color='grey', zorder=4)
plt.fill_between(theta, planet_radius, alpha=0.8, color='grey', label='Radius of Exoplanet', zorder=2)
plt.plot(theta, Earth_radius, color='blue', zorder=3)
plt.fill_between(theta, Earth_radius, alpha=0.5, color='blue', label='Radius of Earth', zorder=1)
# # plt.yticklabels('')
polar_ax.yaxis.grid(False)
polar_ax.xaxis.grid(False)
plt.ylabel("Radius $ \dfrac{r_{planet}}{r_{Earth}} $")
# polar_ax.xaxis('off')
polar_ax.axes.get_xaxis().set_visible(False)
polar_ax.legend(loc=0)

cartesian_ax = plt.subplot(2, 1, 2)

cartesian_ax.plot(s_planet_horizontal, s_planet_vertical, color='grey', ls='-', zorder=1)
cartesian_ax.plot(s_Earth_horizontal, s_Earth_vertical, color='blue', alpha=0.5, ls='--', zorder=2)
plt.ylabel('Height [m]')
plt.xlabel('Horizontal Distance [m]')

cartesian_ax.axvspan(xmin=0.95*bucket_location, xmax=1.05*bucket_location, ymin=0, ymax=0.02, color='blue', alpha=0.3, label='Target Location')
y_limit = max(max(s_planet_vertical), max(s_Earth_vertical))
cartesian_ax.set_ylim(0, 1.5*y_limit)
cartesian_ax.set_xlim(0, 1.5*bucket_location)
plt.legend(['Path of object being projected on the exoplanet', 'Path of the object being projected on Earth', 'Target location between {:.1f}m and {:.1f}m'.format(0.95*bucket_location, 1.05*bucket_location)], loc=0)

st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot(fig=None, clear_figure=None)
