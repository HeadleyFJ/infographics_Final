import streamlit as st


st.set_page_config(
    page_title="Infographic Project",
    page_icon="📡",
    initial_sidebar_state="expanded"
)



st.sidebar.success("Select an Infographic or the Info page.")

st.header("Fin Headley's Infographic Project")

st.text("")
st.text("")
st.text("")


st.write("From the sidebar select one of two infographics.")

st.text("")
st.markdown("***")
st.text("")

st.write("Moons will display all the orbiting moons of any plannet in the solar system.")
st.text("")
st.write("Satellites will display the location of any satellites at any time chosen by the user.")
st.text("")
st.text("")
st.markdown("***")
st.text("")

with st.expander("Acknowledgments"):
    st.write("""
         I would like to thank my entire group, as well as my superviser Chris North, who were an integeral part of this project.""")
    
