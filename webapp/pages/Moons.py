import rebound
import streamlit as st
import datetime
import streamlit.components.v1 as components
import matplotlib.pyplot as plt


st.set_page_config(
    page_title="Moons",
    page_icon="🌕",
)


option = st.selectbox(
    'What planet and its moons would you like to see?',
    ('earth', 'mars', 'jupiter','saturn','uranus','neptune','pluto'))


sim = rebound.Simulation()

if option == 'earth':
    sim.add("399", hash = "Earth")
    sim.add("301", hash = "Moon")

if option =='mars':
    sim.add("499", hash = "Mars")
    sim.add("401")
    sim.add("402")

if option =='jupiter':
    sim.add("599", hash = "Jupiter")
    for i in range(501,554):
        sim.add(str(i))

if option =='saturn':
    sim.add("699", hash = "Saturn")
    for i in range(601,630):
        sim.add(str(i))

if option =='uranus':
    sim.add("799", hash = "Uranus")
    for i in range(701,728):
        sim.add(str(i))

if option =='neptune':
    sim.add("899", hash = "Neptune")
    for i in range(801,814):
        sim.add(str(i))

if option =='pluto':
    sim.add("999", hash = "Pluto")
    for i in range(901,906):
        sim.add(str(i))
        
sim.move_to_com()
op = rebound.OrbitPlotSet(sim,unitlabel="[AU]")
st.header("Selected Planet and Moons")
st.pyplot(op.fig)
st.write("The main plot shows the orbit of the moons around the ecliptic plane of their planet.")
st.write("The top plot shows the orbit of the moons in the X and Z dimentions, relative to the ecliptic plane.")
st.write("The top plot shows the orbit of the moons in the Y and Z dimentions, relative to the ecliptic plane.")
st.write("Taken together, these three plots describe the 3D location of the moon(s) around their host planet.")

