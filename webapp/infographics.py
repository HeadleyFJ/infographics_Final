import streamlit as st


st.set_page_config(
    page_title="Infographic Project",
    page_icon="📡",
    initial_sidebar_state="expanded"
)



st.sidebar.success("Select an Infographic or the Info page.")

st.header("Fin Headley's Infographic Project")

#with st.expander("This talks more about cupcakes."):
#    st.write("""
#Is this an unprofessional way of writing this out?
#Yes... But i need to test if the website works
#and who in their right mind is going to see the 
#innital commit of this project""")


st.write("""
From the sidebar select one of two infographics. 
\n
Satellites will display the location of any satellites at any time chosen by the user.
\n
Moons will display all the orbiting moons of any plannet in the solar system.""")




with st.expander("Acknowledgments"):
    st.write("""
         I would like to thank my entire group, as well as my superviser Chris North, who were an integeral part of this project.""")
    
