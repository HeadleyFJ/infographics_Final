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
ss_name = []
ess_name = []
em_name = []

csv = pd.read_csv("webapp/.data/spaceships_vnc.csv")

sim = rebound.Simulation()
simearth = rebound.Simulation()


st.header("Satellites")

st.write("Pick any date and watch as all satallites listed in the NASA JPL Horizons database are accurately plotted.")


d = st.date_input(
    "Pick a date: (please pick a day, as well as a month and a year)",
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
        name = str(csv.loc[i,'name'])

        interval_start = str(csv.loc[i,'interval_start'])
        interval_end = str(csv.loc[i,'interval_end'])
        date_start = datetime.fromisoformat(interval_start)
        date_end = datetime.fromisoformat(interval_end)

        if date_start<date_check<date_end:
            sim.add(id, hash=id, date = d)
            ess_bodies.append(id)
            ess_body_type.append("Spaceship")
            ess_colour.append("Black")
            ess_name.append(name)

    if str(csv.loc[i,'plot']) == "ss":
        
        id = str(csv.loc[i,'id'])
        name = str(csv.loc[i,'name'])

        interval_start = str(csv.loc[i,'interval_start'])
        interval_end = str(csv.loc[i,'interval_end'])
        date_start = datetime.fromisoformat(interval_start)
        date_end = datetime.fromisoformat(interval_end)

        if date_start<date_check<date_end:
            sim.add(id, hash=id, date = d)
            ss_bodies.append(id)
            ss_body_type.append("Spaceship")
            ss_colour.append("Black")
            ss_name.append(name)

    if str(csv.loc[i,'plot']) == "em":
        
        id = str(csv.loc[i,'id'])
        name = str(csv.loc[i,'name'])
        
        interval_start = str(csv.loc[i,'interval_start'])
        interval_end = str(csv.loc[i,'interval_end'])
        date_start = datetime.fromisoformat(interval_start)
        date_end = datetime.fromisoformat(interval_end)

        if date_start<date_check<date_end:
            simearth.add(id, hash=id, date = d)
            em_bodies.append(id)
            em_body_type.append("Spaceship")
            em_colour.append("Black")
            em_name.append(name)
            satalite = True


if satalite == False:
    simearth.add("301", hash = "Moon", date = d)
    em_bodies.append("Moon")
    em_body_type.append("Moon")
    em_colour.append("Grey")

#never integrate ever!
op1 = rebound.OrbitPlot(simearth, particles = em_bodies,unitlabel="[AU]")
op1.particles.set_color(em_colour)
#for i in range(len(em_body_type)):
  #if em_body_type[i] == "Spaceship":
    #op1.orbits[i].set_linestyle("dashed")

op2 = rebound.OrbitPlot(sim,  particles = ss_bodies,unitlabel="[AU]")
op2.particles.set_color(ss_colour)
#for i in range(len(ss_body_type)):
  #if ss_body_type[i] == "Spaceship":
    #op2.orbits[i].set_linestyle("dashed")
    
op3 = rebound.OrbitPlot(sim,  particles = ess_bodies,unitlabel="[AU]")
op3.particles.set_color(ess_colour)
#for i in range(len(ess_body_type)):
  #if ess_body_type[i] == "Spaceship":
    #op2.orbits[i].set_linestyle("dashed")

col_em, col_ss, col_ess= st.columns(3)
with col_em:
   st.header("Earth-Moon System")
   st.pyplot(op1.fig)
   st.markdown("***")
   st.write("Objects shown:\n")
   st.write("Earth: Star")
   if satalite == False:
        st.write("Moon: Gray")
   st.markdown("***")
   st.write("Satellites:")
   for i in range(len(em_name)):
        st.write(em_name[i])
        
   
with col_ss:
   st.header("Inner Solar System")
   st.pyplot(op2.fig)
   st.markdown("***")
   st.write("Objects shown:\n")
   st.write("Sun: Star")
   if planets:
        st.write("""
        Mercury: Gray   \n
        Venus: Brown    \n
        Earth: Blue \n
        Mars: Red   \n
        """)
   st.markdown("***")
   st.write("Satellites:")
   for i in range(len(ss_name)):
        st.write(ss_name[i])
    
with col_ess:
   st.header("Outer Solar System")
   st.pyplot(op3.fig)
   st.markdown("***")
   st.write("Objects shown:\n")
   st.write("Sun: Star")
   if planets:
        st.write("""
        Jupiter: Orange   \n
        Saturn: Gold    \n
        Uranus: Green \n
        Neptune: Blue   \n
        """)
   st.markdown("***")
   st.write("Satellites:")
   for i in range(len(ess_name)):
        st.write(ess_name[i])

    
    
    
    
