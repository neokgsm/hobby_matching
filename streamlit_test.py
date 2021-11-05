import streamlit as st
st.write(st.session_state)

#if 'ss_list' not in st.session_state:
  #st.session_state.ss_list = []

check1 = st.checkbox('check1', key='check1')
check2 = st.checkbox('check2', key='check2')
check3 = st.checkbox('check3', key='check3')
check4 = st.checkbox('check4', key='check4')
check5 = st.checkbox('check5', key='check5')

def show():
  checked = [k for k, v in st.session_state.items() if v==True]
  st.write(checked)

st.button('Stat...', on_click=show)
