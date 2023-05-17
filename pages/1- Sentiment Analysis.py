# Core Pkgs
import streamlit as st 
import altair as alt
import plotly.express as px 

# EDA Pkgs
import pandas as pd 
import numpy as np 
from datetime import datetime
html_temp = """
<div style ="background-image: linear-gradient(to bottom, #538FFB, #5B54FA);padding:13px">
<h1 style ="color:black;text-align:center;"> NLPify !📔 </h1>
</div>
"""
st.markdown(html_temp, unsafe_allow_html = True)
# Utils
import joblib 
pipe_lr = joblib.load(open("lr_sent.pkl","rb"))


# # Track Utils 
# from track_utils import create_page_visited_table,add_page_visited_details,view_all_page_visited_details,add_prediction_details,view_all_prediction_details,create_emotionclf_table

# Fxn
def predict_emotions(docx):
	results = pipe_lr.predict([docx])
	return results[0] #string

def get_prediction_proba(docx):
	results = pipe_lr.predict_proba([docx])
	return results

emotions_emoji_dict = {"positive":"😃", "negative":"😵‍💫"}
#


# with st.sidebar:
#     selected = option_menu("Main Menu", ["Home", 'Settings'], 
#         icons=['house', 'gear'], menu_icon="cast", default_index=1)
#     selected

# Main Application
# menu = ["Home","About"]
# with st.sidebar:	
#     choice = option_menu("Menu",menu)

st.title("NLPify")



# html_temp = """
# <div style ="background-color:yellow;padding:13px">
# <h1 style ="color:black;text-align:center;">Sentiment Analysis </h1>
# </div>
# """
# st.markdown(html_temp, unsafe_allow_html = True)
	# Title
st.subheader("Sentiment Analysis")
st.markdown("""
	**Sentiment Analysis** is the most common text classification tool that analyses an incoming message 
	and tells whether the underlying sentiment is positive, negative our neutral. You can input a 
	sentence of your choice and gauge the underlying sentiment by playing with the demo here
	""")



	# create_page_visited_table()
	# create_emotionclf_table()

with st.form(key='emotion_clf_form'):
	raw_text = st.text_area("Type your text here .....")
	submit_text = st.form_submit_button(label='Submit')

if submit_text and len(raw_text):
	
	col1,col2  = st.columns(2)

	# Apply Fxn Here
	prediction = predict_emotions(raw_text)
	probability = get_prediction_proba(raw_text)
	
	#add_prediction_details(raw_text,prediction,np.max(probability),datetime.now())
	with col1:
		st.success("Original Text")
		st.write(raw_text)
		st.success("Prediction Probability")
		#st.write(probability)
		proba_df = pd.DataFrame(probability,columns=pipe_lr.classes_) # converting into the classes data drame
		st.write(proba_df.T) # t is transpose
		proba_df_clean = proba_df.T.reset_index()
		proba_df_clean.columns = ["emotions","probability"]

		

		
	with col2:

		st.success("Prediction")
		# st.write(prediction)
		if prediction==1:
			emoji_icon = emotions_emoji_dict["positive"]
			st.write("PREDICTION   |  {}{}".format("Positive",emoji_icon))
		else:
			emoji_icon = emotions_emoji_dict["negative"]
			st.write("PREDICTION   |  {}{}".format("Negative",emoji_icon))

		
		#st.write("PREDICTION   |  {}{}".format(prediction,emoji_icon))
		st.write("CONFIDENCE  |  {}".format(np.max(probability)))
		
		
		fig = alt.Chart(proba_df_clean).mark_bar().encode(x='emotions',y='probability',color='emotions')
		st.altair_chart(fig,use_container_width=True)
elif submit_text and len(raw_text)==0:
	st.write("Please enter valid input")


st.sidebar.subheader("About App")
st.sidebar.text("NLPify App with Streamlit")


st.sidebar.subheader("By")
st.sidebar.text("Ashray Raina - 19bcs021")
st.sidebar.text("Sushant Baarna - 19bcs079")



	# st.sidebar.subheader("About App")
	# st.sidebar.text("NLPiffy App with Streamlit")
	

	# st.sidebar.subheader("By")
	# st.sidebar.text("Rakshit Khajuria - 19bec109")
	# st.sidebar.text("Prikshit Sharma")
				
	# else:
	#     st.markdown('Sentiment Analysis is the most common text classification tool that analyses an incoming message and tells whether the underlying sentiment is positive, negative our neutral. You can input a sentence of your choice and gauge the underlying sentiment by playing with the demo here.')	
