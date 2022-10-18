import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
#%matplotlib inline
import streamlit as st






time = [0,1,2,3,4,5,6,7,8,9,10]
cupcakes = [0,1,1,1,2,4,6,6,8,11,12]

st.header("I HAVE SO MANY CUPCAKES!")

plt.scatter(time,cupcakes,c="black",marker='D',s=50)
plt.xlabel('Time in days')
plt.ylabel('Number of cupcakes I have')

plt.show()

with st.expander("This talks more about cupcakes."):
    st.write("""
Is this an unprofessional way of writing this out?
Yes... But i need to test if the website works
and who in their right mind is going to see the 
innital commit of this project""")
