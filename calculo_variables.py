import funciones_compartidas as f
import streamlit as st
import logica as l
def calculo_variables(tab3):
    def formulario_calculo():
        def mostrar_obtenidos(diccionario, faltante):
            for clave, valor in diccionario.items():
                if valor != diccionario[faltante]:
                    f.entrada_numero(clave, valor)
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
        return resultado
    with tab3:
        st.header("Cálculo de variables")
        formulario_calculo()
        if st.session_state.calcular:
            variable = st.session_state.variable
            calculo = logica_calculo()
            if calculo >= 0:
                if variable == "Rédito o tasa de interés":
                    st.info(f"El {variable.lower()} es {round(calculo*100, 2)}%")
                else:
                    st.info(f"El {variable.lower()} es {round(calculo, 2)}%")
            else:
                st.warning(f"Los datos no son correctos.")