import streamlit as st
from code_templates.java import *
from code_templates.python import *
from code_templates.cpp import *

st.set_page_config(
    page_title="Code Snippets",
    layout="wide",
)

tab1, tab2, tab3 = st.tabs(["Java", "Python", "C++"])

with tab1:
    ct_java_columns()
with tab2:
    ct_python_columns()
with tab3:
    ct_cpp_columns()

