import streamlit as st
import datetime
def inicio():
    def saludo():
        hora_actual = datetime.datetime.now().hour
        if 6 <= hora_actual <= 11:
            return "Buenos días"
        elif 12 <= hora_actual <= 17:
            return "Buenas tardes"
        else:
            return "Buenas noches"
    st.title("¡Bienvenido a Aqevut!")
    st.write("Una aplicación que permite hallar intereses y demás.")
    st.caption("De Gadiel Villavicencio de la Serna")
    st.divider()
    c1, c2 = st.columns(2)
    with c1:
        st.image("inicio/imagen.png")
    with c2:
        st.write(f'''{saludo()}. A continuación le presentamos Aqevut, una
                            calculadora de intereses y montos creada por Gadiel Villavicencio
                            de la Serna.
                            \nAqevut tiene como objetivo facilitar el cálculo de variables
                            relacionadas con el interés, mediante los datos proporcionados
                            por el usuario.''')
    st.markdown('''Aqevut, entre sus usos, posee:
                          \n- Calcular el monto e interés producidos por una letra.
                          \n- Analizar la progresión del monto en periodos.
                          \n- Calcular otras variables relacionadas con el interés.''')
    st.divider()
    st.header("Primeros pasos")
    st.write('''Para comenzar a usar la aplicación, tras entrar en la pestaña 'Cálculo de intereses, 
                podrías intentar por agregar una letra en la barra lateral, introduciendo datos como 
                el capital, el rédito o tasa de interés y el tiempo de duración. Posteriormente, en las pestañas
                Características" y "Análisis", se mostrarán las características y resultados de dicha letra, 
                además de gráficas sobre la progresión del monto producido.''')
inicio()
