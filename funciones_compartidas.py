import streamlit as st
def entrada_numero(texto1, texto2):
    return st.number_input(texto1,
                           min_value=1.00,
                           step=1.00,
                           key=texto2)