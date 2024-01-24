import streamlit as st

st.image('img/neurona.jpg')
st.title('¡Hola neurona!')

tab1, tab2, tab3 = st.tabs(["Una entrada", "Dos entradas", "Tres entradas y sesgo"])



with tab1:
    st.title("Una neurona con una entrada y un peso")
    st.markdown("Peso W <sub>0</sub>", unsafe_allow_html=True)
    w0 = st.slider('p0',0.0, 5.0,label_visibility="collapsed")
    st.markdown("Entrada x <sub>0</sub>", unsafe_allow_html=True)
    x0 = st.number_input('x01',label_visibility="collapsed")
    boton = st.button("Calcular la salida")
    if boton:
        st.write(w0 * x0)


with tab2:
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("Peso W <sub>0</sub>", unsafe_allow_html=True)
        w0 = st.slider('p01',0.0, 5.0,label_visibility="collapsed")
        st.markdown("Peso W <sub>1</sub>", unsafe_allow_html=True)
        w1 = st.slider('p10',0.0, 5.0,label_visibility="collapsed")
    with col2:
        st.markdown("Entrada x <sub>0</sub>", unsafe_allow_html=True)
        x0 = st.number_input('x02',label_visibility="collapsed")
        st.markdown("Entrada x <sub>1</sub>", unsafe_allow_html=True)
        x1 = st.number_input('x10',label_visibility="collapsed")
    boton = st.button("Calcular la salida", key=2)
    if boton:
        st.write(w0 * x0 + w1 * x1)
with tab3:
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("Peso W <sub>0</sub>", unsafe_allow_html=True)
        w0 = st.slider('P02',0.0, 5.0,label_visibility="collapsed")
        st.markdown("Peso W <sub>1</sub>", unsafe_allow_html=True)
        w1 = st.slider('p11',0.0, 5.0,label_visibility="collapsed")
        st.markdown("Peso W <sub>2</sub>", unsafe_allow_html=True)
        w2 = st.slider('p12',0.0,5.0,label_visibility="collapsed")
    with col2:
        st.markdown("Entrada x <sub>0</sub>", unsafe_allow_html=True)
        x0 = st.number_input('x03',label_visibility="collapsed")
        st.markdown("Entrada x <sub>1</sub>", unsafe_allow_html=True)
        x1 = st.number_input('x11',label_visibility="collapsed")
        st.markdown("Entrada x <sub>2</sub>", unsafe_allow_html=True)
        x2 = st.number_input('x2',label_visibility="collapsed")
    
    b = st.number_input("Introduzca el valor del sesgo")
    boton = st.button("Calcular la salida",key=3)
    if boton:
        st.write(w0 * x0 + w1 * x1 + w2 * x2 + b)