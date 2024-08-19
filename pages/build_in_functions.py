import streamlit as st
from build_in_functions.java import *
from build_in_functions.python import *
from build_in_functions.cpp import *

st.set_page_config(
    page_title="Build-In Functions",
    layout="wide",
)

tab1, tab2, tab3 = st.tabs(["Java", "Python", "C++"])

with tab1:
    bif_java_columns()
with tab2:
    bif_python_columns()
with tab3:
    bif_cpp_columns()

