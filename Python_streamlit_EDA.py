# Imports

import streamlit as st
import pandas as pd
import seaborn as sns

st.set_option('deprecation.showPyplotGlobalUse', False)

# 1. Title and Subheaders

st.title('Data Analysis')
st.subheader('Data Analsis Using Python & Streamlit')

#2 Upload Dataset

upload = st.file_uploader("Upload your Dataset(In a CSV format) ")

if upload is not None:
    data = pd.read_csv(upload)

#3 Show Dataset
if upload is not None:

    if st.checkbox("Preview Dataset"):
        if st.button("Head"):
            st.write(data.head())
        if st.button("Tail"):
            st.write(data.tail())



#4 Check DataType of Each Column

if upload is not None:
    if st.checkbox("DataType of Each Column"):
        st.text("DataTypes")
        st.write(data.dtypes)



#5 Find Shape of Our Dataset (Number of Rows And Number of Columns)

if upload is not None:
    data_shape = st.radio("What Dimensions Do You Want To Check?",("Rows","Columns"))
    if data_shape == "Rows":
        st.text("Number Of Rows")
        st.write(data.shape[0])
    if data_shape == "Columns":
        st.text("Number Of Columns")
        st.write(data.shape[1])
   


# 6 Find Null Values in Dataset


if upload is not None:
    test=data.isnull().values.any()
    if test == True:
        if st.checkbox("Null Values in the Dataset"):
            sns.heatmap(data.isnull())
            st.pyplot()

    else:
        st.success("Congrats!!, No Missing Values")

# 7 Find Dulicate Values in Dataset


if upload is not None:
    dup = data.duplicated().any()
    if dup == True:
        st.warning('This Dataset Contains Some Duplicate Values')
        rem_dup = st.selectbox("Do You Want to Remove Duplicate Values?",("Select One", "Yes", "No"))

        if rem_dup == "Yes":
            data = data.drop_duplicates()
            st.text("Duplicate Values are Removed")

        if rem_dup == "No":
            st.text("ok, No Problem")

# 8 Get Overall Statistics

if upload is not None:
    if st.checkbox("Summary of the Dataset"):
        st.write(data.describe())


# 9 About Section

if st.button("About App"):
    st.text("Built With Streamlit")
  

# 10 

if st.checkbox("By"):
    st.success("Abhay K")
    
    st.write("Thanks to Priyang Bhatt. Checkout his Youtube Channel to learn more [link](https://www.youtube.com/@PriyangBhatt/videos)")






