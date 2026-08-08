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
    st.write('''Indica datos necesarios para hallar el monto e interés, analiza los resultados y 
                visualizalos mediante gráficas.''')
    st.caption("De Gadiel Villavicencio de la Serna")
    st.image("inicio/imagen.svg")
    st.write(f'''{saludo()}. A continuación le presentamos Aqevut, una
                                calculadora de intereses y montos creada por Gadiel Villavicencio
                                de la Serna.
                                \nAqevut tiene como objetivo facilitar el cálculo de variables
                                relacionadas con el interés, mediante los datos proporcionados
                                por el usuario.''')
    st.markdown("Aqevut, entre sus usos, posee:")
    c1, c2, c3 = st.columns(3, border = True)
    with c1:
        st.markdown("**📚 Calcular el interés**")
        st.write("Poder calcular el interés y el monto resultante de la letra agregada.")
    with c2:
        st.markdown("**📈 Obtener gráficas de la progresión del monto**")
        st.write("Tener a disposición gráficas que indiquen cómo progresa el monto de periodo en periodo")
    with c3:
        st.markdown("**🧮 Calcular variables relacionadas al interés**")
        st.write('''Se pueden calcular variables relacionadas como el capital, tiempo de duración y rédito o
                    también llamado tasa de interés.''')
    st.divider()
    st.header("Primeros pasos")
    st.markdown('''1. Dirigirse a la pestaña "Calculadora de intereses".
                   \n 2. Ir a la barra lateral y agregar una letra.
                   \n 3. Listo. Ya estarían los gráficos sobre la progresión del monto y los resultados
                   de la letra financiera.''')
inicio()
