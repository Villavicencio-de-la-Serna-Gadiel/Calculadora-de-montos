import streamlit as st
import pandas as pd
import logica as l
def en_session_state(nombre, valor):
    if nombre not in st.session_state:
        st.session_state[nombre] = valor
    return st.session_state[nombre]
def analisis(tab2):
    def mostrar_graficos(diccionario):
        grafico_lineas, grafico_barras, grafico_areas = \
            st.tabs(["Gráfico de líneas", "Gráfico de barras", "Gráfico de áreas"])
        dt = pd.DataFrame(l.para_graficos(diccionario))
        with grafico_lineas:
            st.line_chart(dt, x = "Montos", y = "Periodos")
        with grafico_barras:
            st.bar_chart(dt, x = "Montos", y = "Periodos")
        with grafico_areas:
            st.area_chart(dt, x = "Montos", y = "Periodos")
    def logica_filtros():
        if "registrar" in st.session_state:
            if st.session_state.registrar:
                if st.session_state.forma_filtro == "Monto":
                    mayor_monto = st.session_state.mayor_monto
                    menor_monto = st.session_state.menor_monto
                    if mayor_monto > menor_monto:
                        resultado = l.recorrer_diccionario(diccionario=progresion_monto,
                                                           clave_valor="clave",
                                                           minimo=menor_monto,
                                                           maximo=mayor_monto)
                        st.session_state.filtrado = resultado
                        st.session_state.con_filtro = True
                    else:
                        st.session_state.advertencia = "El menor monto no puede ser mayor al mayor monto."
                else:
                    mayor_periodo = st.session_state.mayor_periodo
                    menor_periodo = st.session_state.menor_periodo
                    if mayor_periodo > menor_periodo:
                        resultado = l.recorrer_diccionario(diccionario=progresion_monto,
                                                           clave_valor="valor",
                                                           minimo=menor_periodo,
                                                           maximo=mayor_periodo)
                        st.session_state.filtrado = resultado
                        st.session_state.con_filtro = True
                    else:
                        st.session_state.advertencia = "El menor periodo no puede ser mayor al mayor periodo."
        if "quitar_filtros" in st.session_state:
            if st.session_state.quitar_filtros:
                st.session_state.con_filtro = False
    def formulario_filtros():
        with st.expander("Filtros"):
            forma_filtro = st.radio("Forma de filtro",
                                    options=["Periodo",
                                             "Monto"],
                                    key = "forma_filtro")
            with st.form("Filtro"):
                if forma_filtro == "Periodo":
                    progresion_valores = progresion_monto.values()
                    menor_valor = min(progresion_valores)
                    mayor_valor = max(progresion_valores)
                    st.slider("Menor periodo",
                              min_value=menor_valor,
                              max_value=mayor_valor,
                              key = "menor_periodo")

                    st.slider("Mayor periodo",
                              min_value=menor_valor,
                              max_value=mayor_valor,
                              key = "mayor_periodo")
                else:
                    progresion_claves = progresion_monto.keys()
                    menor_clave = min(progresion_claves)
                    mayor_clave = max(progresion_claves)
                    st.slider("Menor monto",
                              min_value=menor_clave,
                              max_value=mayor_clave,
                              key = "menor_monto")
                    st.slider("Mayor monto",
                              min_value=menor_clave,
                              max_value=mayor_clave,
                              key = "mayor_monto")
                st.form_submit_button("Registrar",
                                      key="registrar")
            st.button("Quitar filtros",
                      key = "quitar_filtros")
    with tab2:
        st.header("Análisis")
        if "letra" in st.session_state:
            progresion_monto = st.session_state.letra.progresion_monto()
            logica_filtros()
            con_filtro = en_session_state("con_filtro", False)
            if con_filtro:
                filtrado = st.session_state.filtrado
                mostrar_graficos(filtrado)
            else:
                mostrar_graficos(progresion_monto)
            if len(progresion_monto) > 1:
                formulario_filtros()
                if "advertencia" in st.session_state:
                    st.warning(st.session_state.advertencia)
                    st.session_state.pop("advertencia")