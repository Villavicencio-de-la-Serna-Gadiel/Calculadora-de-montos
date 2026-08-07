from funciones_compartidas import *
from . import logica as l
import streamlit as st
def calculo_variables_intereses():
    def formulario_calculo():
        def mostrar_obtenidos(diccionario, faltante):
            for clave, valor in diccionario.items():
                if valor != diccionario[faltante]:
                    entrada_numero(clave, valor)
        categoria = st.radio("Interés",
                             options = ["Simple",
                                        "Compuesto"],
                             key = "categoria_entrada")
        variable = st.selectbox("Variable",
                                options = ["Capital",
                                           "Rédito o tasa de interés",
                                           "Tiempo de duración"],
                                key = "variable")
        nombres_datos = {"Capital": "capital_entrada",
                         "Rédito o tasa de interés": "redito_entrada",
                         "Tiempo de duración": "tiempo_entrada",
                         "Monto": "monto_entrada"}
        with st.form("Datos obtenidos"):
            if categoria == "Simple":
                mostrar_obtenidos(nombres_datos, variable)
            else:
                mostrar_obtenidos(nombres_datos, variable)
                st.toggle("Capitalización continua",
                          key="capitalizacion_entrada")
            st.form_submit_button("Calcular",
                                  on_click = logica_calculo,
                                  key = "calcular")
    def logica_calculo():
        variable = st.session_state.variable
        monto = st.session_state.monto_entrada
        if variable == "Capital":
            redito = st.session_state.redito_entrada/100
            tiempo = st.session_state.tiempo_entrada
            if st.session_state.categoria_entrada == "Simple":
                resultado = l.LetraSimple(capital = "",
                                          redito = redito,
                                          tiempo = tiempo).faltante(monto)
            else:
                capitalizacion = st.session_state.capitalizacion_entrada
                resultado = l.LetraCompuesta(capital="",
                                             redito=redito,
                                             tiempo=tiempo,
                                             capitalizacion=capitalizacion).faltante(monto)
        elif variable == "Rédito o tasa de interés":
            capital = st.session_state.capital_entrada
            tiempo = st.session_state.tiempo_entrada
            if st.session_state.categoria_entrada == "Simple":
                resultado = l.LetraSimple(capital = capital,
                                          redito = "",
                                          tiempo = tiempo).faltante(monto)
            else:
                capitalizacion = st.session_state.capitalizacion_entrada
                resultado = l.LetraCompuesta(capital=capital,
                                             redito="",
                                             tiempo=tiempo,
                                             capitalizacion=capitalizacion).faltante(monto)
        else:
            capital = st.session_state.capital_entrada
            redito = st.session_state.redito_entrada/100
            if st.session_state.categoria_entrada == "Simple":
                resultado = l.LetraSimple(capital = capital,
                                          redito = redito,
                                          tiempo = "").faltante(monto)
            else:
                capitalizacion = st.session_state.capitalizacion_entrada
                resultado = l.LetraCompuesta(capital=capital,
                                             redito=redito,
                                             tiempo="",
                                             capitalizacion=capitalizacion).faltante(monto)
        en_session_state("resultado", resultado)
    st.subheader("Cálculo de variables relacionadas al interés")
    formulario_calculo()
    if st.session_state.calcular:
        tipo_variable = st.session_state.variable
        calculo = st.session_state.resultado
        if calculo >= 0:
            if tipo_variable == "Rédito o tasa de interés":
                st.info(f"El {tipo_variable.lower()} es {round(calculo * 100, 2)}%")
            else:
                st.info(f"El {tipo_variable.lower()} es {round(calculo, 2)}")
        else:
            st.warning(f"Los datos no son correctos.")
def diferencia_fechas():
    def formulario_fechas():
        with st.form("Fechas"):
            fecha_inicial =  st.date_input("Fecha inicial",
                                           key="fecha_inicial")
            fecha_final = st.date_input("Fecha final",
                                         key="fecha_final")
            hallar_tiempo = st.form_submit_button("Hallar tiempo transcurrido",
                                      on_click = logica_fechas,
                                      key="hallar_tiempo")
        if hallar_tiempo:
            if fecha_final == fecha_inicial:
                st.warning("Las fechas inicial y final no pueden ser iguales.")
            elif fecha_inicial > fecha_final:
                st.warning("La fecha inicial no puede ser mayor a la fecha final.")
            else:
                st.session_state.presionado = True
    def mostrar_columnas():
        diferencia_tiempo_dias = st.session_state.diferencia_tiempo_dias
        c1, c2 = st.columns(2)
        with c2:
            st.selectbox("Unidad de tiempo",
                         options = l.unidades_tiempo_admisibles(diferencia_tiempo_dias),
                         key = "unidad_medida")
            print(st.session_state.unidad_medida)
        with c1:
            with st.container(border = True):
                print(st.session_state.unidad_medida)
                st.write(str(round(l.conversion_unidad_tiempo(tiempo = diferencia_tiempo_dias,
                                                              unidad = st.session_state.unidad_medida), 2)))
    def logica_fechas():
        fecha_inicial = st.session_state.fecha_inicial
        fecha_final = st.session_state.fecha_final
        st.session_state.diferencia_tiempo_dias = l.tiempo_transcurrido(fecha_inicial=fecha_inicial,
                                                                        fecha_final=fecha_final)
    st.subheader("Diferencia de fechas")
    formulario_fechas()
    if "presionado" in st.session_state:
        mostrar_columnas()
def calculo_variables(tab):
    with tab:
        st.header("Cálculo de variables")
        st.divider()
        calculo_variables_intereses()
        diferencia_fechas()