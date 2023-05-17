# Core Pkgs
import streamlit as st 
import altair as alt
import plotly.express as px 

# EDA Pkgs
import pandas as pd 
import numpy as np 
from datetime import datetime

def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url(https://www.linkpicture.com/q/logo_19.png);
                background-repeat: no-repeat;
                padding-top: 120px;
                background-position: 20px 20px;
            }
            [data-testid="stSidebarNav"]::before {
                content: "NLPify";
                margin-left: 20px;
                margin-top: 20px;
                font-size: 30px;
                position: relative;
                top: 100px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

add_logo()


html_temp = """
<div style ="background-image: linear-gradient(to bottom, #538FFB, #5B54FA);padding:13px">
<h1 style ="color:black;text-align:center;"> NLPify !📔 </h1>
</div>
"""
st.markdown(html_temp, unsafe_allow_html = True)

st.image('logo/logo_00432.png', width=705)

	# Title
st.subheader("Natural Language Processing On the Go..")
st.markdown("""
	#### Description
	+ This is a Natural Language Processing(NLP) Based App useful for basic NLP task Tokenization, NER, Sentiment and Summarization.

	""")

from PIL import Image,ImageFilter,ImageEnhance

if st.checkbox("Model Architecture"):
    st.image('arch.png')

st.sidebar.subheader("By")
st.sidebar.text("Ashray Raina - 19bcs021")
st.sidebar.text("Sushant Baarna - 19bcs079")



