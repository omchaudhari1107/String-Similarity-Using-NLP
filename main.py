import streamlit as st
import spacy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt

# Load Spacy model
nlp = spacy.load("en_core_web_sm")

# Function to preprocess text
def preprocess(text):
    doc = nlp(text)
    filtered_tokens = []
    for token in doc:
        if token.is_punct:
            continue
        filtered_tokens.append(token.lemma_)
    
    return " ".join(filtered_tokens) 

# Function to return vectorized array
def ReturnArray(lst):
    v = CountVectorizer(ngram_range=(1, 1))
    v.fit_transform(lst)
    return v.transform(lst).toarray()

# Streamlit app
def main():
    st.title('Text Similarity Analyzer using CV')

    text1 = st.text_input('Text 1','I am a devloper')
    text2 = st.text_input('Text 2','I am enthusiastic devloper')

    if st.button('Calculate Similarity'):
        str_preprocessed = [preprocess(text1), preprocess(text2)]

        vectorized_data = ReturnArray(str_preprocessed)
        similarity_matrix = cosine_similarity(vectorized_data)
        similarity_score = round(similarity_matrix[0, 1], 2)
        difference_score = round(1 - similarity_score, 2)

        labels = [f'{similarity_score*100:.2f}% Similarity', f'{difference_score*100:.2f}% Non-Similarity']
        scores = [similarity_score, difference_score]
        colors = ['green', 'red']

        fig, ax = plt.subplots()
        ax.bar(labels, scores, color=colors)
        ax.set_ylim(0, 1)
        ax.set_ylabel('Scores')
        ax.set_title('Cosine Similarity')
        st.pyplot(fig)

if __name__ == '__main__':
    main()
