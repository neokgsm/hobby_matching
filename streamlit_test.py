import streamlit as st
st.write(st.session_state)

if 'ss_list' not in st.session_state:
  st.session_state.ss_list = []

def append(selected):
  st.session_state.ss_list.append(selected)

hobby_list = ['a', 'b', 'c']

selected = st.selectbox('pick one', hobby_list)

st.button('add', on_click=append(selected))
  
