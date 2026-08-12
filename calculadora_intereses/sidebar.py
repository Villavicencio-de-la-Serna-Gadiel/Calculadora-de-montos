from . import logica as l
from funciones_compartidas import entrada_numero
import streamlit as st
def sidebar_financiero():
    def cambiar_letra():
        def formulario_interes_simple():
            entrada_numero("Capital",
                           "capital")
            entrada_numero("Rédito o tasa de interés",
                           "redito")
            entrada_numero("Tiempo de duración",
                           "tiempo")
        def formulario_interes_compuesto():
            formulario_interes_simple()
            st.toggle("Capitalización continua",
                      key="capitalizacion")
        def registrar_letra():
            capital = st.session_state.capital
            redito = st.session_state.redito / 100
            tiempo = st.session_state.tiempo
            if categoria == "Simple":
                letra = l.LetraSimple(capital=capital,
                                      redito=redito,
                                      tiempo=tiempo)
            else:
                if st.session_state.capitalizacion:
                    capitalizacion = "capitalización continua"
                else:
                    capitalizacion = "capitalización no continua"
                letra = l.LetraCompuesta(capital=capital,
                                         redito=redito,
                                         tiempo=tiempo,
                                         capitalizacion=capitalizacion)
            st.session_state.letra = letra
        with st.expander("Agregar letra"):
            categoria = st.radio("Interés",
                                 options = ["Simple",
                                            "Compuesto"])
            with st.form("Interés"):
                if categoria == "Simple":
                    formulario_interes_simple()
                else:
                    formulario_interes_compuesto()
                registrar = st.form_submit_button("Registrar",
                                                  on_click=registrar_letra)
            if registrar:
                st.success("Registrado con éxito")
            st.caption("Los valores deben estar en las mismas unidades")
    with st.sidebar:
        st.title("Opciones")
        cambiar_letra()