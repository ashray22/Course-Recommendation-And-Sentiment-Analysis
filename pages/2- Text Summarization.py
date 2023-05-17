# # Function to Analyse Tokens and Lemma
# # Core Pkgs
# import streamlit as st 
# import os
# import nltk
# nltk.download('punkt')

# # NLP Pkgs
# from textblob import TextBlob 
# import spacy
# from gensim.summarization.summarizer import summarize
# # Sumy Summary Pkg
# from sumy.parsers.plaintext import PlaintextParser
# from sumy.nlp.tokenizers import Tokenizer
# from sumy.summarizers.lex_rank import LexRankSummarizer
# html_temp = """
# <div style ="background-color:yellow;padding:13px">
# <h1 style ="color:black;text-align:center;"> NLPify !📔 </h1>
# </div>
# """
# st.markdown(html_temp, unsafe_allow_html = True)
# # Function for Sumy Summarization
# def sumy_summarizer(docx):
# 	parser = PlaintextParser.from_string(docx,Tokenizer("english"))
# 	lex_summarizer = LexRankSummarizer()
# 	summary = lex_summarizer(parser.document,3)
# 	summary_list = [str(sentence) for sentence in summary]
# 	result = ' '.join(summary_list)
# 	return result


# def main():
#     	# Title

# 	st.subheader("Text summarization")
# 	st.markdown("""
#     	Text summarization is the problem of reducing the number of sentences and words
#         of a document without changing its meaning. There are different techniques to 
#         extract information from raw text data and use it for a summarization model, 
#         overall they can be categorized as Extractive and Abstractive. Extractive
#         methods select the most important sentences within a text (without necessarily understanding the meaning),
#         therefore the result summary is just a subset of the full text.
#         On the contrary, Abstractive models use advanced NLP (i.e. word embeddings)
#          to understand the semantics of the text and generate a meaningful summary.
#         Consequently, Abstractive techniques are much harder to train from scratch as they need a lot of parameters and data. 
#     	""")

#         	# Summarization
# 	if st.checkbox("Show Text Summarization"):
# 		st.subheader("Summarize Your Text")

# 		message = st.text_area("Enter Text","Type Here ..")
# 		summary_options = st.selectbox("Choose Summarizer",['sumy','gensim'])
# 		if st.button("Summarize"):
# 			if summary_options == 'sumy':
# 				st.text("Using Sumy Summarizer ..")
# 				summary_result = sumy_summarizer(message)
# 			elif summary_options == 'gensim':
# 				st.text("Using Gensim Summarizer ..")
# 				summary_result = summarize(message)
# 			else:
# 				st.warning("Using Default Summarizer")
# 				st.text("Using Gensim Summarizer ..")
# 				summary_result = summarize(message)

		
# 			st.success(summary_result)
# st.sidebar.subheader("About App")
# st.sidebar.text("NLPify App with Streamlit")


# st.sidebar.subheader("By")
# st.sidebar.text("Rakshit Khajuria - 19bec109")
# st.sidebar.text("Prikshit Sharma - 19bec062")


# if __name__ == '__main__':
#   	main()
import streamlit as st
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
html_temp = """
<div style ="background-image: linear-gradient(to bottom, #538FFB, #5B54FA);padding:13px">
<h1 style ="color:black;text-align:center;"> NLPify !📔 </h1>
</div>
"""
st.markdown(html_temp, unsafe_allow_html = True)

# Streamlit app title and instructions
st.title("Text Summarizer App")
st.write("Enter a piece of text and the app will generate a summary.")

# Text input
text = st.text_area("Enter Text", "")

# Summarize button
if st.button("Summarize"):
    # Check if text is empty
    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        # Initialize the summarizer
        summarizer = LexRankSummarizer()
        parser = PlaintextParser.from_string(text, Tokenizer("english"))

        # Generate summary
        summary_sentences = summarizer(parser.document, 3)  # Change the number to control the summary length

        # Combine summary sentences into a single string
        summary = " ".join([str(sentence) for sentence in summary_sentences])

        # Display summary
        st.subheader("Summary")
        st.write(summary)
        
st.sidebar.subheader("By")
st.sidebar.text("Ashray Raina - 19bcs021")
st.sidebar.text("Sushant Baarna - 19bcs079")
# Function to Analyse Tokens and Lemma
# Core Pkgs
# import streamlit as st 
# import os


# # NLP Pkgs
# from textblob import TextBlob 
# import spacy
# from gensim.summarization import summarize

# Sumy Summary Pkg
# from sumy.parsers.plaintext import PlaintextParser
# from sumy.nlp.tokenizers import Tokenizer
# from sumy.summarizers.lex_rank import LexRankSummarizer
# html_temp = """
# <div style ="background-color:yellow;padding:13px">
# <h1 style ="color:black;text-align:center;"> NLPify !📔 </h1>
# </div>
# """
# st.markdown(html_temp, unsafe_allow_html = True)
# # Function for Sumy Summarization
# def sumy_summarizer(docx):
# 	parser = PlaintextParser.from_string(docx,Tokenizer("english"))
# 	lex_summarizer = LexRankSummarizer()
# 	summary = lex_summarizer(parser.document,3)
# 	summary_list = [str(sentence) for sentence in summary]
# 	result = ' '.join(summary_list)
# 	return result


# def main():
#     	# Title

# 	st.subheader("Text summarization")
# 	st.markdown("""
#     	Text summarization is the problem of reducing the number of sentences and words
#         of a document without changing its meaning. There are different techniques to 
#         extract information from raw text data and use it for a summarization model, 
#         overall they can be categorized as Extractive and Abstractive. Extractive
#         methods select the most important sentences within a text (without necessarily understanding the meaning),
#         therefore the result summary is just a subset of the full text.
#         On the contrary, Abstractive models use advanced NLP (i.e. word embeddings)
#          to understand the semantics of the text and generate a meaningful summary.
#         Consequently, Abstractive techniques are much harder to train from scratch as they need a lot of parameters and data. 
#     	""")

#         	# Summarization
# 	if st.checkbox("Show Text Summarization"):
# 		st.subheader("Summarize Your Text")

# 		message = st.text_area("Enter Text","Type Here ..")
# 		summary_options = st.selectbox("Choose Summarizer",['sumy','gensim'])
# 		if st.button("Summarize"):
# 			if summary_options == 'sumy':
# 				st.text("Using Sumy Summarizer ..")
# 				summary_result = sumy_summarizer(message)
# 			elif summary_options == 'gensim':
# 				st.text("Using Gensim Summarizer ..")
# 				summary_result = summarize(message)
# 			else:
# 				st.warning("Using Default Summarizer")
# 				st.text("Using Gensim Summarizer ..")
# 				summary_result = summarize(message)

		
# 			st.success(summary_result)
# st.sidebar.subheader("About App")
# st.sidebar.text("NLPify App with Streamlit")


# st.sidebar.subheader("By")
# st.sidebar.text("Ashray Raina - 19bcs021")


# if __name__ == '__main__':
# 	main()
