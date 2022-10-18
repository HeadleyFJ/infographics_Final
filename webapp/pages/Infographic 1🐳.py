import streamlit as st

st.title("this is a different page")

st.header("this is a different header")

st.header("this is a button")

if st.button('This is a button'):
    st.write('Pressed')
else:
    st.write('Not Pressed')
   
  
st.header("this is a checkbox")
  
checkbox = st.checkbox('check this box')

if checkbox:
    st.write('you did it!')
    
