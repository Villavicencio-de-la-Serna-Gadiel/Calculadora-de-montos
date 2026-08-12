from calculadora_intereses import (calculo_variables as c,
                                   datos as da,
                                   analisis as a,
                                   sidebar as s)
import streamlit as st
def titulos():
    st.title("Calculadora de intereses")
    st.write('''Escribe las características de una letra y halla el monto,
                   ya sea causado por interés simple o compuesto.''')
titulos()
s.sidebar_financiero()
datos, analisis, calculo_variables = st.tabs(["Datos",
                                              "Análisis",
                                              "Cálculo de variables"])
da.datos(datos)
a.analisis(analisis)
c.calculo_variables(calculo_variables)