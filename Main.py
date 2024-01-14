import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np


st.set_page_config(page_title="streamlit-tuto",
                   layout="wide",
                   initial_sidebar_state="auto")

st.header("Data Visualisation")

file = st.file_uploader("Upload your file",type=["csv"])
if file is not None :
    df   = pd.read_csv(file,encoding= "latin-1")
    nrows= st.slider("Choose the number of rows",5,max_value= len(df))
    ncolums = st.multiselect("Select the columns",df.columns.to_list(),default= df.columns.to_list())
    st.write(df[:nrows][ncolums])
    num_col = df.select_dtypes(include=np.number).columns.to_list()
    tab1 , tab2 , tab3 ,tabs4= st.tabs(["scatter","histogram","box","pie chart"])
    
    with tab1 :
        col1 , col2 , col3,col4 = st.columns(4)
        with col1 :
            X = st.selectbox("Select the column X ",num_col)
        with col2 :   
            Y = st.selectbox("Select the column Y" ,num_col)
        with col3 :
            color = st.selectbox("Select the color" , df.columns,None)
        with col4:
            size = st.selectbox("Select the size",num_col , None )
        plot = px.scatter(df,x= X , y= Y,color=color,size= size)
        st.plotly_chart(plot)
    with tab2 :
        X = st.selectbox("Select the column",df.columns)
        hist = px.histogram(df,x= X)
        st.plotly_chart(hist)
    with tab3 :
        Y = st.selectbox("Select the column Y " ,df.columns)
        X = st.selectbox("Select the column X  ",df.columns)
        pairplot = px.box(df,x=X,y=Y)
        st.plotly_chart(pairplot)
    with tabs4 :
        name = st.selectbox("Select the name",df.columns)
        values = st.selectbox("Select the value",num_col)
        pie = px.pie(df,names=name,values=values)
        st.plotly_chart(pie)
        