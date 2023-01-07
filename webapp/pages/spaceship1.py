import rebound
import streamlit as st
import pandas as pd
from datetime import datetime
import streamlit.components.v1 as components
import matplotlib.pyplot as plt


st.set_page_config(
    page_title="Satellites",
    page_icon="🛰",
    initial_sidebar_state="expanded",
    layout="wide"
)



ss_body_type = []
ss_colour = []
ess_colour = []
ess_body_type = []
ss_bodies = []
ess_bodies = []
em_bodies = []
em_body_type = []
em_colour = []

csv = pd.read_csv("webapp/.data/spaceships_vnc.csv")

sim = rebound.Simulation()

simearth = rebound.Simulation()


d = st.date_input(
    "Pick a date",
    #value = datetime.today(),min_value = datetime.fromisoformat("1960-01-01"))
    value = datetime.fromisoformat("1950-01-01"),min_value = datetime.fromisoformat("1950-01-01"),max_value = datetime.fromisoformat("2027-01-01"))
d = str(d)

date_check = datetime.fromisoformat(d)

satalite = False

st.write("Planets")
planets = st.checkbox('Planets', value = True)
   
sim.add("Sun",date=d)

simearth.add("Earth",date=d)
#em_bodies.append("Earth")
#em_body_type.append("Planet")
#em_colour.append("Blue")

if planets:
   sim.add("199", hash = "Mercury", date = d)
   ss_bodies.append("Mercury")
   ss_body_type.append("Planet")
   ss_colour.append("Gray") 
   sim.add("299", hash = "Venus", date = d)
   ss_bodies.append("Venus")
   ss_body_type.append("Planet")
   ss_colour.append("Brown") 
   sim.add("399", hash = "Earth", date = d)
   ss_bodies.append("Earth")
   ss_body_type.append("Planet")
   ss_colour.append("Blue")
   sim.add("499", hash = "Mars", date = d)
   ss_bodies.append("Mars")
   ss_body_type.append("Planet")
   ss_colour.append("Red") 
   sim.add("599", hash = "Jupiter", date = d)
   ess_bodies.append("Jupiter")
   ess_body_type.append("Planet")
   ess_colour.append("Orange") 
   sim.add("699", hash = "Saturn", date = d)
   ess_bodies.append("Saturn")
   ess_body_type.append("Planet")
   ess_colour.append("Gold") 
   sim.add("799", hash = "Uranus", date = d)
   ess_bodies.append("Uranus")
   ess_body_type.append("Planet")
   ess_colour.append("Green") 
   sim.add("899", hash = "Neptune", date = d)
   ess_bodies.append("Neptune")
   ess_body_type.append("Planet")
   ess_colour.append("Blue") 


for i in range(len(csv)):
    if str(csv.loc[i,'plot']) == "ess":
        
        id = str(csv.loc[i,'id'])

        interval_start = str(csv.loc[i,'interval_start'])
        interval_end = str(csv.loc[i,'interval_end'])
        date_start = datetime.fromisoformat(interval_start)
        date_end = datetime.fromisoformat(interval_end)

        if date_start<date_check<date_end:
            sim.add(id, hash=id, date = d)
            ess_bodies.append(id)
            ess_body_type.append("Spaceship")
            ess_colour.append("Black")

    if str(csv.loc[i,'plot']) == "ss":
        
        id = str(csv.loc[i,'id'])

        interval_start = str(csv.loc[i,'interval_start'])
        interval_end = str(csv.loc[i,'interval_end'])
        date_start = datetime.fromisoformat(interval_start)
        date_end = datetime.fromisoformat(interval_end)

        if date_start<date_check<date_end:
            sim.add(id, hash=id, date = d)
            ss_bodies.append(id)
            ss_body_type.append("Spaceship")
            ss_colour.append("Black")

    if str(csv.loc[i,'plot']) == "em":
        
        id = str(csv.loc[i,'id'])

        interval_start = str(csv.loc[i,'interval_start'])
        interval_end = str(csv.loc[i,'interval_end'])
        date_start = datetime.fromisoformat(interval_start)
        date_end = datetime.fromisoformat(interval_end)

        if date_start<date_check<date_end:
            simearth.add(id, hash=id, date = d)
            em_bodies.append(id)
            em_body_type.append("Spaceship")
            em_colour.append("Black")
            satalite = True


if satalite == False:
    simearth.add("301", hash = "Moon", date = d)
    em_bodies.append("Moon")
    em_body_type.append("Moon")
    em_colour.append("Grey")

#never integrate ever!
op1 = rebound.OrbitPlot(simearth, particles = em_bodies)
op1.particles.set_color(em_colour)
#for i in range(len(em_body_type)):
  #if em_body_type[i] == "Spaceship":
    #op1.orbits[i].set_linestyle("dashed")

op2 = rebound.OrbitPlot(sim,  particles = ss_bodies)
op2.particles.set_color(ss_colour)
#for i in range(len(ss_body_type)):
  #if ss_body_type[i] == "Spaceship":
    #op2.orbits[i].set_linestyle("dashed")
    
op3 = rebound.OrbitPlot(sim,  particles = ess_bodies)
op3.particles.set_color(ess_colour)
#for i in range(len(ess_body_type)):
  #if ess_body_type[i] == "Spaceship":
    #op2.orbits[i].set_linestyle("dashed")

col_em, col_ss, col_ess= st.columns(3)
with col_em:
   st.header("Earth Moon System")
   st.pyplot(op1.fig)
with col_ss:
   st.header("Solar System")
   st.pyplot(op2.fig)
with col_ess:
   st.header("Extra Solar System")
   st.pyplot(op3.fig)
