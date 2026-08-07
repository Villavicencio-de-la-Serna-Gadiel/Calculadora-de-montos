import streamlit as st
def entrada_numero(texto1, texto2):
    return st.number_input(texto1,
                           placeholder = texto1,
                           min_value=1.00,
                           step=1.00,
                           key=texto2)
def en_session_state(nombre, valor):
    if nombre not in st.session_state:
        st.session_state[nombre] = valor
    return st.session_state[nombre]