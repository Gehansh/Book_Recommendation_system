import streamlit as st
import pickle
import numpy as np
#import pandas as pd

pivot_table = pickle.load(open('pivot_table.pkl','rb'))
similarity_score = pickle.load(open('similarity_score.pkl','rb'))
books = pickle.load(open('books.pkl','rb'))
popularDF = pickle.load(open('popular_df.pkl','rb'))
def recommend(selected_book):
    # fetch index
    index = np.where(pivot_table.index == selected_book)[0][0]
    similar_items = sorted(list(enumerate(similarity_score[index])), key=lambda x: x[1], reverse=True)[1:11]

    data = []
    for i in similar_items:
        item = []
        temp_df = books[books['Book-Title'] == pivot_table.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-L'].values))

        data.append(item)
    return data



books_list = pickle.load(open('fam_books.pkl','rb'))

st.title("Books Recommendation System")
Selected_Book_Name = st.selectbox(
    'Search the Book',
    books_list)

if st.button('Recommend'):
    data=recommend(Selected_Book_Name)
    #ct=0
    #"""for i in st.columns(10,gap="small"):
    #    st.write(data[ct][0])
    #    st.write(data[ct][1])
    #    st.image(data[ct][2])
    #    ct=ct+1"""

    col1, col2, col3  = st.columns(3,gap="large")

    with col1:
        st.write(data[0][0])
        st.caption(data[0][1])
        st.image(data[0][2])

    with col2:
        st.write(data[1][0])
        st.caption(data[1][1])
        st.image(data[1][2])

    with col3:
        st.write(data[2][0])
        st.caption(data[2][1])
        st.image(data[2][2])

    st.write('\n')


    col4, col5, col6=st.columns(3,gap="small")
    with col4:
        st.write(data[3][0])
        st.caption(data[3][1])
        st.image(data[3][2])

    with col5:
        st.write(data[4][0])
        st.caption(data[4][1])
        st.image(data[4][2])

    with col6:
        st.write(data[5][0])
        st.caption(data[5][1])
        st.image(data[5][2])

    col7, col8, col9 = st.columns(3)
    with col7:
        st.write(data[6][0])
        st.caption(data[6][1])
        st.image(data[6][2])

    with col8:
        st.write(data[7][0])
        st.caption(data[7][1])
        st.image(data[7][2])

    with col9:
        st.write(data[8][0])
        st.caption(data[8][1])
        st.image(data[8][2])
