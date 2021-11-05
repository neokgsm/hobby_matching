import streamlit as st
st.write(st.session_state)

if 'ss_list' not in st.session_state:
  st.session_state.ss_list = []

def update():
  if 'check1' not in st.session_state.ss_list:
    st.session_state.ss_list.append('check1')
  elif 'check1' in st.session_state.ss_list:
    st.session_state.ss_list.remove('check1')


check1 = st.checkbox('check1', key='check1')
check2 = st.checkbox('check2', key='check2')
