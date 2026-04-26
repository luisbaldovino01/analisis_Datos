import pandas as pd
import streamlit as st
import plotly.express as px
from limpieza import limpiar_dataset


with st.spinner("Cargando datos... :)"):
    dataset = pd.read_excel("icfes_depto_sucre.xlsx")

tab1, tab2 = st.tabs(['Exploración','Limpieza'])

with tab1:

    st.subheader("Vista previa del dataset")

    # TOTAL DE FILAS Y COLUMNAS
    filas, columnas = dataset.shape 
    st.write(f"El dataset tiene {filas} filas y {columnas} columnas")

    st.dataframe(dataset.head(50)) #mostrar el dataset
    
    # TIPOS DE DATOS DEL DATASET
    st.subheader("Tipos de datos")
    st.write(dataset.dtypes)
    
    # REGISTROS POR PERIODOS
    st.subheader("Registros por peridos")
    registrosp = dataset.groupby(["PERIODO"]).size().sort_index()
    st.write(registrosp)

    # CULUMNAS CON CAMPOS NULOS
    st.subheader("Columnas con valores nulos")
    nulos = dataset.isnull().sum()
    st.write(nulos[nulos > 0].sort_values(ascending=False))


    # COLUMNAS A TRABAJAR
    st.subheader("Columnas a trabajar")
    categorias = ["FAMI_ESTRATOVIVIENDA", "FAMI_EDUCACIONMADRE", "FAMI_EDUCACIONPADRE", "FAMI_TIENEINTERNET", "FAMI_TIENECOMPUTADOR" ,"COLE_AREA_UBICACION", "COLE_NATURALEZA", "ESTU_GENERO"]

    for columna in categorias:
        st.write(f"Columna: {columna}")
        
        st.write(dataset[columna].value_counts())
        
        st.write("Cantidad de categorías únicas: ", dataset[columna].nunique())

    # DISTRIBUCION DEL PUNTAJE GLOBAL
    fig = px.histogram(dataset, x="PUNT_GLOBAL",nbins=30, title="Distribucion del puntaje global")
    st.plotly_chart(fig)

with tab2:
    st.subheader("Limpieza de datos")

    dataset_limpio = limpiar_dataset(dataset)
    
    filas, columnas = dataset_limpio.shape
    st.write(f"El dataset tiene {filas} filas y {columnas} columnas")
    st.write("Vista previa del dataset limpio")
    st.write(dataset_limpio.head(10))


