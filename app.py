# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 22:09:33 2024

@author: PC
"""

import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st
import pickle


popular_df = pickle.load(open(r"C:\Users\PC\data science\popular.pkl",'rb'))
pt = pickle.load(open(r"C:\Users\PC\data science\pt.pkl",'rb'))
books = pickle.load(open(r"C:\Users\PC\data science\books.pkl",'rb'))
similarity_scores = pickle.load(open(r"C:\Users\PC\data science\similarity_scores.pkl",'rb'))

def welcome():
    return "Welcome All"


def recommend(user_input):
    
    index = np.where(pt.index==user_input)[0][0]
    similar_items = sorted(list(enumerate(similarity_scores[index])),key=lambda x:x[1],reverse=True)[1:5]
    
    data = []
    for i in similar_items:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
        
        data.append(item)
    
    return data

def main():
    st.header('Book Recommender System Using Machine Learning')
    st.subheader('Welcome All')

    user_input = st.text_input("Enter the book name", "Harry Potter")  # Default example input

    if st.button("Recommend"):
        recommendations = recommend(user_input)
        st.write("Here are some book recommendations for you:")
        for rec in recommendations:
            st.write(f"Title: {rec[0]}, Author: {rec[1]}")
            st.image(rec[2])

if __name__ == '__main__':
    main()


    