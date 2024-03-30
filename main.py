import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    response = requests.get(url)
    data = response.json()
    full_path = "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    return full_path


def recommend(selected_movie):
    index = movies[movies['title'] == selected_movie].index[0]
    distances = similarity[index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]
    recommend_movies = []
    recommend_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommend_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API
        recommend_movies_posters.append(fetch_poster(movie_id))
    return recommend_movies ,recommend_movies_posters

st.title("Movie Recommender System")

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))


selected_movie_name = st.selectbox("Select A Movie", movies['title'].values)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
        st.text(names[5])
        st.image(posters[5])
    with col2:
        st.text(names[1])
        st.image(posters[1])
        st.text(names[6])
        st.image(posters[6])
    with col3:
        st.text(names[2])
        st.image(posters[2])
        st.text(names[7])
        st.image(posters[7])
    with col4:
        st.text(names[3])
        st.image(posters[3])
        st.text(names[8])
        st.image(posters[8])
    with col5:
        st.text(names[4])
        st.image(posters[4])
        st.text(names[9])
        st.image(posters[9])




