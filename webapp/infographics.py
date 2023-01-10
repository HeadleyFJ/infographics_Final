import streamlit as st


st.set_page_config(
    page_title="Infographic Project",
    page_icon="📡",
    initial_sidebar_state="expanded"
)



st.sidebar.success("Select an Infographic or the Info page.")

st.header("PXT991 Infographics")

st.text("")
st.text("")

st.write("Fin Headley")
st.text("")
st.text("")


st.write("From the sidebar select one of two infographics.")

st.text("")
st.markdown("***")
st.text("")

st.write("Moons will display all the orbiting moons for any planet in the solar system.")
st.text("")
st.write("Satellites will display the location of all satellites at a time chosen by the user.")
st.text("")
st.text("")
st.markdown("***")
st.text("")

with st.expander("Acknowledgments"):
    st.write("""
         I would like to thank my partner Adam Threlfall, 
         as well as my entire group, Benjamin Fry, Charlie Brayson, 
         Helena Krabberoed, pallavi Sati, Shachar Jacobson, 
         Sharath Kunhim Veedu Nambiar, as well as my superviser Chris North, 
         who were all an intergeral part of this project.""")
    
