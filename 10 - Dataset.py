# Core Pkgs
import streamlit as st 
import altair as alt
import plotly.express as px 

# EDA Pkgs
import pandas as pd 
import numpy as np 
from datetime import datetime


op_df = pd.read_csv('Final_Project\data\data.csv')
st.dataframe(op_df)
st.download_button('Download CSV', op_df.to_csv(), mime = 'data/csv',file_name='data.csv')