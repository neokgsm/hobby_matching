import streamlit as st
st.write(st.session_state)

if 'ss_list' not in st.session_state:
  st.session_state.ss_list = []

def update():
  if 'check1' not in st.session_state.ss_list and check1:
    st.session_state.ss_list.remove('check1')
  elif 'check1' in st.session_state.ss_list and not check1:
    st.session_state.ss_list.append('check1')


check1 = st.checkbox('check1', on_change=update)
