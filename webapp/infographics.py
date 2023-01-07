import streamlit as st


st.set_page_config(
    page_title="Infographic Project",
    page_icon="📡",
    initial_sidebar_state="expanded"
)


st.write("[![Star](<https://img.shields.io/github/stars/><HeadleyFJ>/<infographics_Final>.svg?logo=github&style=social)](<https://gitHub.com/><HeadleyFJ>/<infographics_Final>)")

st.sidebar.success("Select an Infographic or the intro page.")

st.header("Fin Headley's infographic Project")


with st.expander("This talks more about cupcakes."):
    st.write("""
Is this an unprofessional way of writing this out?
Yes... But i need to test if the website works
and who in their right mind is going to see the 
innital commit of this project""")

st.write("""
         also i have 8 versions of python and
         none of them want to play nice
         so i am havinng to write all the code in github
         and this is less than idea for me
         as there is really no way for me to test things""")
    
