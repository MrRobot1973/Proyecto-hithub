import streamlit as st
import login as login


st.header("RedTube")
login.generarLogin()
if 'usuario' in st.session_state:
    st.header('Página :orange[principal]')
    st.subheader('Información página principal')
