from funciones_compartidas import en_session_state
from calculadora_normal import logica as l
import streamlit as st
def calculadora(tab):
    def aniadir(simbolo):
        st.session_state.entrada += simbolo
    def logica_botones():
        if "retroceso" in st.session_state:
            if st.session_state.retroceso:
                st.session_state.entrada = st.session_state.entrada[:-1]
        if "eliminar" in st.session_state:
            if st.session_state.eliminar:
                st.session_state.entrada = ""
                st.session_state.calculo = ""
        if "calcular" in st.session_state:
            if st.session_state.calcular:
                st.session_state.calculo = l.calcular(st.session_state.entrada)
    def mostrar_botones():
        numeros_signos = list(range(0, 10)) + ["+", "-", "×", "÷", ".", "(", ")"]
        con_funcionalidad = ["retroceso","eliminar", "calcular"]
        lista = numeros_signos + con_funcionalidad
        c1, c2, c3 = st.columns(3)
        columnas = [c1, c2, c3]
        i = 0
        for simbolo in lista:
            with columnas[i//7]:
                if simbolo in numeros_signos:
                    if type(simbolo) == int:
                        simbolo = str(simbolo)
                    st.button(simbolo,
                              on_click = aniadir,
                              args = (simbolo,),
                              width = "stretch")
                else:
                    if simbolo == "retroceso":
                        st.button(simbolo,
                                  key = "retroceso",
                                  width = "stretch")
                    elif simbolo == "eliminar":
                        st.button(simbolo,
                                  key = "eliminar",
                                  width = "stretch")
                    elif simbolo == "calcular":
                        st.button(simbolo,
                                  key = "calcular",
                                  width = "stretch")
            i += 1
    with tab:
        with st.container(border = True,
                          width = 400):
            logica_botones()
            with st.container(border = True):
                calculo = en_session_state("calculo", "")
                st.latex(en_session_state("entrada", ""))
                if type(calculo) in [int, float] or calculo == "":
                    st.caption(calculo)
                else:
                    if type(calculo) == list:
                        st.caption(calculo[0],
                                    help = calculo[1])
                    else:
                        st.caption(calculo)
            with st.container(border = True):
                mostrar_botones()
