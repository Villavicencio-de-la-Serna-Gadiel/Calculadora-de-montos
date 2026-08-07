import streamlit as st
def configuracion():
    st.set_page_config(page_title = "Aqevut|Calculadora de intereses",
                       page_icon = "📊")
configuracion()
paginas = st.navigation(pages = [st.Page(page = "inicio\\inicio.py",
                                         title = "Inicio"),
                                 st.Page(page = "calculadora_normal\\calculadora_normal.py",
                                         title = "Calculadora normal"),
                                 st.Page(page = "calculadora_intereses\\calculadora_intereses.py",
                                         title = "Calculadora de intereses")],
                        position = "top")
paginas.run()