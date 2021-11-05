import streamlit as st
st.write(st.session_state)

if 'ss_list' not in st.session_state:
  st.session_state.ss_list = []

def append():
  ss_list.append("Clicked!")

st.write()
st.button('button', on_click=append)
  
