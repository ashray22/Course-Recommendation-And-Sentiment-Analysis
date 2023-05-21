#Importing Core Packages
from operator import index
import streamlit as st
import streamlit.components.v1 as stc

#Load EDA
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity,linear_kernel

html_temp = """
<div style ="background-image: linear-gradient(to bottom, #538FFB, #5B54FA);padding:13px">
<h1 style ="color:black;text-align:center;"> NLPify !📔 </h1>
</div>
"""
st.markdown(html_temp, unsafe_allow_html = True)


#Load Dataset
def load_data(data):
        df = pd.read_csv(data)
        return df
#Vectorize & Cosine Similarity Matrix

def vectorize_text_to_cosine_matrix(data):
       count_vect = CountVectorizer()
       cv_matrix = count_vect.fit_transform(data)
       #Get the cosine
       cosine_sim_matrix = cosine_similarity(cv_matrix)
       return cosine_sim_matrix

@st.cache_data

def get_recommendation(title, cosine_sim_matrix, df, num_of_rec=10):
    course_indices = pd.Series(df.index, index=df['course_title']).drop_duplicates()
    idx = course_indices[title]
    sim_scores = list(enumerate(cosine_sim_matrix[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    selected_course_indices = [i[0] for i in sim_scores[0:num_of_rec+1]]
    selected_course_scores = [i[1] for i in sim_scores[0:num_of_rec+1]]
    result_df = df.iloc[selected_course_indices]
    result_df['similarity_score'] = selected_course_scores
    final_recommended_course = result_df[['course_title', 'similarity_score', 'url', 'price', 'duration']]
    return final_recommended_course

#Function
RESULT_TEMP = """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300&display=swap" rel="stylesheet">
<div style="width:90%;height:100%;margin:1px;padding:5px;position:relative;border-radius:5px;border-bottom-right-radius: 60px;
box-shadow:0 0 4px 2px #ccc; background-image: linear-gradient(to bottom, #538FFB, #5B54FA); ;
  border-left: 5px ; font-family: 'Montserrat', sans-serif;">
<h1>{}</h1>
<p style="color:black;"><span style="color:black; font-weight:bold">📈Score::</span>{}</p>
<p style="color:red;"><span style="red:black;font-weight:bold">🔗</span><a href="{}" target="_blank">Link</a></p>


<p style="color:black;"><span style="color:black;font-weight:bold">💲Price:</span>{}</p>
<p style="color:black"><span style="color:black;font-weight:bold">⌚ Duration:</span>{}</p>

</div>
"""
#Search for Course  #a8f0c6    #6c6c6c
@st.cache_data
def search_term_if_not_found(term,df):
      result_df = df[df['course_title'].str.contains(term)]
      return result_df


def main():
	st.title("Course Recommendation App")
	
menu = ["Home","Recommend","About"]
choice = st.sidebar.selectbox("Menu",menu)

df = load_data(r"data/final_data.csv")

if choice == "Home":
        st.subheader("Home")
        st.dataframe(df.head(10))

elif choice == "Recommend":
        st.subheader("Recommend Courses")
        cosine_sim_matrix = vectorize_text_to_cosine_matrix(df['course_title'])

    
        search_term  = st.selectbox('Search!!',df['course_title'].values)
        num_of_rec = st.sidebar.number_input("Number of Recomendations",4,100,5)
        if st.button("Recommend"):
            if search_term is not None:
                try:
                    results = get_recommendation(search_term,cosine_sim_matrix,df,num_of_rec)
                    with st.expander("Results as JSON"):
                        results_json = results.to_dict('index')
                        st.write(results_json)
                    for row in results.iterrows():
                        rec_title = row[1][0]
                        rec_score = row[1][1]
                        rec_url = row[1][2]
                        rec_price = row[1][3]
                        rec_duration = row[1][4]
                        #st.write("Title",rec_title,)
                        
                        stc.html(RESULT_TEMP.format(rec_title,rec_score,rec_url,rec_price, rec_duration),height=350)
                except:
                    results = "Not Found"
                    st.warning(results)
                    st.info("Suggested Options Include")
                    result_df = search_term_if_not_found(search_term,df)
                    st.dataframe(result_df)
                    
else:
        st.subheader("About")
        st.text("Built with Streamlit")
        

if __name__ == '_main_':
	main()