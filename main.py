import streamlit as st
import pandas

# from folder.filename import function_name
from services.barchart import display_barchart
from services.hist import display_histogram
st.title("My first streamlit website")

upload_file = st.file_uploader("Upload a dataset",type=['csv'])

if upload_file is not None:
    data = pandas.read_csv(upload_file)
    st.write(data)

    all_columns= data.columns.tolist()
    selected_col = st.selectbox('Select a column', all_columns)

    if pandas.api.types.is_numeric_dtype(data[selected_col]):
        st.write('Selected Column ',selected_col," is numeric")
        display_histogram(data[selected_col])
    else:
        st.write('Selected Column ',selected_col," is nominal")
        display_barchart(data[selected_col])
