import pandas as pd
import plotly.express as px
import streamlit as st
import pickle
import numpy as np

wage = pd.read_csv("Salario1.csv")

st.title("Aplicación 4")
tab1, tab2, tab3 = st.tabs(["Análisis univariado", "Análisis bivariado", "Modelo"])
with tab1:
    fig6 = px.histogram ( wage, x = "Educación" )
    fig7 = px . histogram ( wage, x = "Estado civil" )
    fig8 = px . histogram ( wage, x = "Años en la empresa" )
    fig9 = px . histogram ( wage, x = "Genero" )
    fig10= px . histogram ( wage, x = "Experiencia" )
    fig11= px . histogram ( wage, x = "Salario" )
    st.plotly_chart(fig6)
    st.plotly_chart(fig7)
    st.plotly_chart(fig8)
    st.plotly_chart(fig9)
    st.plotly_chart(fig10)
    st.plotly_chart(fig11)
with tab2:
    fig1  =  px.scatter(wage ,  x = "Educación" ,  y = "Salario" ,  title = 'Salario respecto a educación' ) 
    fig2  =  px.histogram(wage ,  x = "Estado civil" ,  y = "Salario" ,  title = 'Salario respecto a si está casad@' )
    fig3  =  px.histogram(wage ,  x = "Genero" ,  y = "Salario" ,  title = 'Salario respecto a género' )
    fig4 =  px.scatter(wage ,  x = "Experiencia" ,  y = "Salario" ,  title = "Salario respecto a la experiencia")
    fig5 =  px.scatter(wage ,  x = "Años en la empresa" ,  y = "Salario" ,  title = "Salario respecto a los años en la empresa")
    st.plotly_chart(fig1)
    st.plotly_chart(fig2)
    st.plotly_chart(fig3)
    st.plotly_chart(fig4)
    st.plotly_chart(fig5)
with tab3:
    with open("model.pickle", "rb") as m:
        modelo = pickle.load(m)
    educ = st.slider("Seleccione los años de educación", 0, 18)
    exper = st.slider("Seleccione años de experiencia", 1, 51)
    tenure = st.slider("Seleccione años trabajados dentro de la empresa", 0 ,44)
    gender = st.selectbox("Seleccione genero", ["Mujer", "Hombre"])
    if gender == "Mujer":
            gender = 1
    else:
            gender = 0
    

    married = st.selectbox("Seleccione estado civil", ["Casado","Soltero"])
    if married == "Casado":
            married = 1
    else:
            married = 0


    if st.button("Predecir"):
        pred = modelo.predict(np.array([[educ, exper, tenure, gender, married]]))
        st.write(pred[0])