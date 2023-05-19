# Function to Analyse Tokens and Lemma
# Core Pkgs
import streamlit as st 
import os


# NLP Pkgs
#from textblob import TextBlob 
import spacy
#from gensim.summarization import summarize

# Sumy Summary Pkg
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

html_temp = """
<div style ="background-image: linear-gradient(to bottom, #538FFB, #5B54FA);padding:13px">
<h1 style ="color:black;text-align:center;"> NLPify !📔 </h1>
</div>
"""
st.markdown(html_temp, unsafe_allow_html = True)
@st.cache_data
def entity_analyzer(my_text):
	nlp = spacy.load('en_core_web_sm')
	docx = nlp(my_text)
	tokens = [ token.text for token in docx]
	entities = [(entity.text,entity.label_)for entity in docx.ents]
	allData = ['"Token":{},\n"Entities":{}'.format(tokens,entities)]
	return allData

def main():
    	# Title
	st.subheader("Named Entity Recognition")
	st.markdown("""
    	**Named Entity Recognition** - Named entity recognition (NER) — sometimes referred to as entity chunking, 
        extraction, or identification — is the task of identifying and categorizing key information 
        (entities) in text. An entity can be any word or series of words that consistently refers to the same thing. 
        Every detected entity is classified into a predetermined category. For example, 
        an NER machine learning (ML) model might detect the word “super.AI” in a text and classify it as a “Company”.  
    	""")
	# Entity Extraction
	if st.checkbox("Show Named Entities"):
		st.subheader("Analyze Your Text")

		message = st.text_area("Enter Text","Type Here ..")
		if st.button("Extract"):
			entity_result = entity_analyzer(message)
			st.json(entity_result)

st.sidebar.subheader("About App")
st.sidebar.text("NLPify App with Streamlit")


st.sidebar.subheader("By")
st.sidebar.text("Ashray Raina - 19bcs021")
#st.sidebar.text("Sushant Baarna - 19bcs079")




if __name__ == '__main__':
	main()
