import rebound
import streamlit as st
import datetime
import streamlit.components.v1 as components
import matplotlib.pyplot as plt



option = st.selectbox(
    'What planet\'s moons would you like to see',
    (earth, mars, jupiter,saturn,uranus,neptune,pluto))


sim = rebound.Simulation()

if option == earth:
    sim.add("399", hash = "Earth")
    sim.add("301", hash = "Moon")

if option ==mars:
    sim.add("499", hash = "Mars")
    sim.add("401")
    sim.add("402")

if option ==jupiter:
    sim.add("599", hash = "Jupiter")
    for i in range(501,554):
        sim.add(str(i))

if option ==saturn:
    sim.add("699", hash = "Saturn")
    for i in range(601,654):
        sim.add(str(i))

if option ==uranus:
    sim.add("799", hash = "Uranus")
    for i in range(701,728):
        sim.add(str(i))

if option ==neptune:
    sim.add("899", hash = "Neptune")
    for i in range(801,814):
        sim.add(str(i))

if option ==pluto:
    sim.add("999", hash = "Pluto")
    for i in range(901,906):
        sim.add(str(i))

op = rebound.OrbitPlot(sim)
st.header("moons")
st.pyplot(op.fig)
