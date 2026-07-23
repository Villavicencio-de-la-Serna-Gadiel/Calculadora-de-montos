import streamlit as st
def datos(tab1):
    def columnas_resultado():
        c1, c2 = st.columns(2)
        with c1:
            st.metric("Interés",
                      value = round(letra.interes(letra.monto()), 2))
        with c2:
            st.metric("Monto",
                      value = round(letra.monto(), 2))
    def columnas_interes_simple():
        c1, c2, c3 = st.columns(3)
        with c1:
            st.metric("Capital",
                      value=round(letra.capital, 2))
        with c2:
            st.metric("Rédito",
                      value=f"{round(letra.redito*100, 2)}%")
        with c3:
            st.metric("Tiempo",
                      value=round(letra.tiempo, 2))
    def columnas_interes_compuesto():
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            st.metric("Capital",
                      value=round(letra.capital, 2))
        with c2:
            st.metric("Rédito",
                      value=f"{round(letra.redito*100, 2)}%")
        with c3:
            st.metric("Tiempo",
                      value=round(letra.tiempo, 2))
        with c4:
            if letra.capitalizacion == "capitalización continua":
                es_continua = "Sí"
            else:
                es_continua = "No"
            st.metric("Capitalización continua",
                      value=es_continua)
    with tab1:
        if "letra" in st.session_state:
            letra = st.session_state.letra
            st.header("Datos")
            st.subheader("Características de la letra")
            with st.expander("Características"):
                if not hasattr(letra, "capitalizacion"):
                    columnas_interes_simple()
                else:
                    columnas_interes_compuesto()
            st.subheader("Resultados de la letra")
            with st.expander("Resultados"):
                columnas_resultado()