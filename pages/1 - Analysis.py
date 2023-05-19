import streamlit as st
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image,ImageFilter,ImageEnhance

html_temp = """
<div style ="background-image: linear-gradient(to bottom, #538FFB, #5B54FA);padding:13px">
<h1 style ="color:black;text-align:center;"> NLPify !📔 </h1>
</div>
"""


st.markdown(html_temp, unsafe_allow_html = True)
# Title and Subheader
st.title("Sentiment EDA App")
st.subheader("EDA Web App with Streamlit ")

my_dataset = "data/clean_data.csv"
my_dataset_before = "data/raw_data.csv"

@st.cache_data
def explore_data_before(dataset):
	df = pd.read_csv(os.path.join(dataset))
	return df 

@st.cache_data
def explore_data(dataset):
	df = pd.read_csv(os.path.join(dataset))
	return df 
# To Improve speed and cache data
if st.checkbox("RAW DATA "):
# Show Dataset
    if st.checkbox("Preview DataFrame"):
        data = explore_data(my_dataset_before)
        if st.button("Head"):
            st.write(data.head())
        if st.button("Tail"):
            st.write(data.tail())
        else:
            st.write(data.head(2))

    # Show Entire Dataframe
    if st.checkbox("Show All DataFrame"):
        data = explore_data(my_dataset_before)
        st.dataframe(data)


    # Show Description
    if st.checkbox("Show All Column Name"):
        data = explore_data(my_dataset_before)
        st.text("Columns:")
        st.write(data.columns)
    
        # Dimensions
    data_dim = st.radio('What Dimension Do You Want to Show',('Rows','Columns'))
    if data_dim == 'Rows':
        data = explore_data(my_dataset_before)
        st.text("Showing Length of Rows")
        st.write(len(data))
    if data_dim == 'Columns':
        data = explore_data(my_dataset_before)
        st.text("Showing Length of Columns")
        st.write(data.shape[1])




if st.checkbox("Preprocessed dataset"):
# Show Dataset
    if st.checkbox("Preview DataFrame "):
        data = explore_data(my_dataset)
        if st.button("Head"):
            st.write(data.head())
        if st.button("Tail"):
            st.write(data.tail())
        else:
            st.write(data.head(2))

    # Show Entire Dataframe
    if st.checkbox("Show All DataFrame "):
        data = explore_data(my_dataset)
        st.dataframe(data)


    # Show Description
    if st.checkbox("Show All Column Name "):
        data = explore_data(my_dataset)
        st.text("Columns:")
        st.write(data.columns)

    # Dimensions
    data_dim = st.radio('What Dimension Do You Want to Show ',('Rows','Columns'))
    if data_dim == 'Rows':
        data = explore_data(my_dataset)
        st.text("Showing Length of Rows")
        st.write(len(data))
    if data_dim == 'Columns':
        data = explore_data(my_dataset)
        st.text("Showing Length of Columns")
        st.write(data.shape[1])

if st.checkbox("WordCloud for positive reviews."):
    st.image(Image.open('images/positive.png'), caption='Sunrise by the mountains')

if st.checkbox("WordCloud for negative reviews."):
    st.image(Image.open('images/neg.png'), caption='Sunrise by the mountains')

# if st.checkbox("Show Summary of Dataset"):
# 	data = explore_data(my_dataset)
# 	st.write(data.describe())

# Show Plots
import altair as alt
# Show Plots
# Show Plots
col1,col2  = st.columns(2)
with col1:
    if st.checkbox("Simple Bar Plot with Matplotlib for Review Ratings "):
        data = explore_data(my_dataset)
        fig = plt.figure(figsize=(20, 10))
        sns.countplot(x="score", data=data)
        plt.title("Simple Bar Plot with Matplotlib for Review Ratings ", fontsize=14)
        st.pyplot(fig)   


    if st.checkbox("Simple Bar Plot with Matplotlib for Sentiments"):
        data = explore_data(my_dataset)
        fig = plt.figure(figsize=(10, 4))
        sns.countplot(x="sentiment", data=data)
        st.pyplot(fig)

    if st.checkbox("Simple Bar Plot with Matplotlib for Review Ratings w.r.t Sentiments"):
        data = explore_data(my_dataset)
        fig = plt.figure(figsize=(10, 4))
        sns.countplot(x="score", data=data,hue='sentiment')
        plt.title("Simple Bar Plot with Matplotlib for Review Ratings ", fontsize=14)
        st.pyplot(fig)






import plotly.express as px
import plotly.offline

with col2:
    if st.checkbox("Simple Bar Plot with Matplotlib for Review Ratings  "):
        data = explore_data(my_dataset)
        fig = px.pie(data, names='score', title='Simple Bar Plot with Matplotlib for Review Ratings',color_discrete_sequence=px.colors.sequential.RdBu)
        fig.show()

    if st.checkbox("Simple Bar Plot with Matplotlib for Review Sentiment   "):
        data = explore_data(my_dataset)
        fig = px.pie(data, names='sentiment', title='Population of European continent',color_discrete_sequence=px.colors.sequential.RdBu)
        fig.show()

    if st.checkbox("Simple Bar Plot with Matplotlib for Review Ratings w.r.t Sentiments   "):
        data = explore_data(my_dataset)
        fig = px.sunburst(data, title='Simple Bar Plot with Matplotlib for Review Ratings',path=['score','sentiment'],color_discrete_sequence=px.colors.sequential.RdBu)
        fig.show()
        # # fig = plt.figure(figsize=(20, 10))
        # plt.pie(x="score", data=data)
        # plt.title("Simple Bar Plot with Matplotlib for Review Ratings ", fontsize=14)
        # st.pyplot(fig)   
from PIL import Image,ImageFilter,ImageEnhance
if st.checkbox("Logistic Regression Confusion Matrix"):
    st.image(Image.open('images/filename.png'), caption='Sunrise by the mountains')

if st.checkbox("Logistic Regression Classification Report"):
    st.image(Image.open('images/classification_report.png'), caption='Sunrise by the mountains')

# if st.checkbox("Simple Bar Plot with Matplotlib for Sentiments__"):
    #     data = explore_data(my_dataset)
    #     fig = plt.figure(figsize=(10, 4))
    #     sns.countplot(x="sentiment", data=data)
    #     st.pyplot(fig)

    # if st.checkbox("Simple Bar Plot with Matplotlib for Review Ratings w.r.t Sentiments___"):
    #     data = explore_data(my_dataset)
    #     fig = plt.figure(figsize=(10, 4))
    #     sns.countplot(x="score", data=data,hue='sentiment')
    #     plt.title("Simple Bar Plot with Matplotlib for Review Ratings ", fontsize=14)
    #     st.pyplot(fig)



# # Show Plots
# if st.checkbox("Simple Correlation Plot with Matplotlib "):
# 	data = explore_data(my_dataset)
# 	plt.matshow(data.corr())
# 	st.pyplot()

# # Show Plots
# if st.checkbox("Simple Correlation Plot with Seaborn "):
# 	data = explore_data(my_dataset)
# 	st.write(sns.heatmap(data.corr(),annot=True))
# 	# Use Matplotlib to render seaborn
# 	st.pyplot()

# # Show Plots
# if st.checkbox("Bar Plot of Groups or Counts"):
# 	data = explore_data(my_dataset)
# 	v_counts = data.groupby('species')
# 	st.bar_chart(v_counts)


# # Iris Image Manipulation
# @st.cache
# def load_image(img):
# 	im =Image.open(os.path.join(img))
# 	return im

# # Image Type
# species_type = st.radio('What is the Iris Species do you want to see?',('Setosa','Versicolor','Virginica'))

# if species_type == 'Setosa':
# 	st.text("Showing Setosa Species")
# 	st.image(load_image('imgs/iris_setosa.jpg'))
# elif species_type == 'Versicolor':
# 	st.text("Showing Versicolor Species")
# 	st.image(load_image('imgs/iris_versicolor.jpg'))
# elif species_type == 'Virginica':
# 	st.text("Showing Virginica Species")
# 	st.image(load_image('imgs/iris_virginica.jpg'))

st.sidebar.subheader("About App")
st.sidebar.text("NLPify App with Streamlit")


st.sidebar.subheader("By")
st.sidebar.text("Ashray Raina - 19bcs021")
#st.sidebar.text("Sushant Baarna - 19bcs079")

