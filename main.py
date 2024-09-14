import streamlit as st
import pandas
st.title("My first streamlit website")

upload_file = st.file_uploader("Upload a dataset",type=['csv'])

if upload_file is not None:
    data = pandas.read_csv(upload_file)
    st.write(data)

    all_columns= data.columns.tolist()
    selected_col = st.selectbox('Select a column', all_columns)

    if pandas.api.types.is_numeric_dtype(data[selected_col]):
        st.write('Selected Column ',selected_col," is numeric")
    else:
        st.write('Selected Column ',selected_col," is nominal")
