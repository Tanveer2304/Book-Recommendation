# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 22:09:33 2024

@author: PC
"""


import numpy as np
import streamlit as st
import pickle


popular_df = pickle.load(open('popular.pkl','rb'))
pt = pickle.load(open('pt.pkl','rb'))
books = pickle.load(open('books.pkl','rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl','rb'))

def welcome():
    return "Welcome All"


def recommend(book_name):
    # Check if book_name exists in pt.index
    if book_name not in pt.index:
        print(f"Book '{book_name}' not found.")
        return []
    
    # Find index of book_name in pt.index
    index = np.where(pt.index == book_name)[0][0]
    
    # Fetch similar items based on similarity_scores
    similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:5]
    
    data = []
    for i, score in similar_items:
        item = []
        # Find details of similar books in 'books' DataFrame
        temp_df = books[books['Book-Title'] == pt.index[i]]
        item.extend(temp_df.drop_duplicates('Book-Title')['Book-Title'].values)
        item.extend(temp_df.drop_duplicates('Book-Title')['Book-Author'].values)
        item.extend(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values)
        
        data.append(item)
    
    return data


def main():
    st.header('Book Recommender System Using Machine Learning')
    st.subheader('Welcome All')

    user_input = st.text_input("Enter the book name", "1984")  # Default example input

    if st.button("Recommend"):
        recommendations = recommend(user_input)
        st.write("Here are some book recommendations for you:")
        for rec in recommendations:
            st.write(f"Title: {rec[0]}, Author: {rec[1]}")
            st.image(rec[2])

if __name__ == '__main__':
    main()


    
