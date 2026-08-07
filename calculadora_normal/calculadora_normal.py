from calculadora_normal import modo_normal as m
import streamlit as st
def titulos():
    st.title("Calculadora normal")
    st.write("Efectua operaciones simples.")
titulos()
modo_normal, modo_cientifico = st.tabs(["Modo normal", "Modo científico"])
m.calculadora(modo_normal)
with modo_cientifico:
    st.info("Podría agregarse en el futuro.")