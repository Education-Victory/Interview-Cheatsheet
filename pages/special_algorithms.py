import streamlit as st
from special_algorithms.java import *
from special_algorithms.python import *
from special_algorithms.cpp import *

st.set_page_config(
    page_title="Special Algorithms",
    layout="wide",
)

tab1, tab2, tab3 = st.tabs(["Java", "Python", "C++"])

with tab1:
    sa_java_columns()
with tab2:
    sa_python_columns()
with tab3:
    sa_cpp_columns()

