import funciones_compartidas as f
import calculo_variables as c
import streamlit as st
import analisis as an
import logica as l
import datos as d
def configuracion():
    st.set_page_config(page_title = "Capiter|Calculadora de intereces",
                       page_icon = "📊")
def titulos():
    st.title("Calculadora de montos")
    st.write('''Escribe las características de una letra y halla el monto,
                ya sea causado por interés simple o compuesto.''')
    st.caption("De Gadiel Villavicencio de la Serna")
def sidebar():
    def caracteristicas_letra():
        def formulario_interes_simple():
            f.entrada_numero("Capital",
                           "capital")
            f.entrada_numero("Rédito o tasa de interés",
                           "redito")
            f.entrada_numero("Tiempo de duración",
                           "tiempo")
        def formulario_interes_compuesto():
            formulario_interes_simple()
            st.toggle("Capitalización continua",
                      key="capitalizacion")
        with st.expander("Agregar letra"):
            categoria = st.radio("Interés",
                                 options = ["Simple",
                                            "Compuesto"])
            with st.form("Interés"):
                if categoria == "Simple":
                    formulario_interes_simple()
                else:
                    formulario_interes_compuesto()
                registrar = st.form_submit_button("Registrar")
            if registrar:
                capital = st.session_state.capital
                redito = st.session_state.redito/100
                tiempo = st.session_state.tiempo
                st.success("Registrado con éxito")
                if categoria == "Simple":
                    letra = l.LetraSimple(capital = capital,
                                          redito = redito,
                                          tiempo = tiempo)
                else:
                    if st.session_state.capitalizacion:
                        capitalizacion = "capitalización continua"
                    else:
                        capitalizacion = "capitalización no continua"
                    letra = l.LetraCompuesta(capital = capital,
                                             redito = redito,
                                             tiempo = tiempo,
                                             capitalizacion = capitalizacion)
                st.session_state.letra = letra
            st.caption("Los valores deben estar en las mismas unidades")
    with st.sidebar:
        st.title("Opciones")
        caracteristicas_letra()
configuracion()
titulos()
sidebar()
tab1, tab2, tab3 = st.tabs(["Datos", "Análisis", "Cálculo de variables"])
d.datos(tab1)
an.analisis(tab2)
c.calculo_variables(tab3)
