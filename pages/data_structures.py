import streamlit as st
from data_structures.java import *
from data_structures.python import *
from data_structures.cpp import *

st.set_page_config(
    page_title="Data Structures",
    layout="wide",
)

tab1, tab2, tab3 = st.tabs(["Java", "Python", "C++"])

with tab1:
    ds_java_columns()
with tab2:
    ds_python_columns()
with tab3:
    ds_cpp_columns()
