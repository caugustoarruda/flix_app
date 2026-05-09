import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
import requests


movies = [
    {
        'id': 1,
        'name': 'Titanic'
    }
]
def show_movies():
    st.write("Page filmes")
    # token = requests.post(url='http://127.0.0.1:8000/api/v1/authentication/token/', json={
    #     "username": "carruda",
    #     "password": "Root@2026"
    # })
    # access = token.json().get('access')
    # headers = {
    #     'Authorization': f'Bearer {access}'
    # }
    # genres = requests.get(url='http://127.0.0.1:8000/api/v1/movies/', headers=headers)
    # print(genres.json())


    AgGrid(pd.DataFrame(movies))

    # st.title('Cadastrar novo movies:')
    # name = st.text_input('Nome do movie')
    # if st.button('Cadastrar'):
    #     movies.append(
    #         {
    #             'id': len(movies) + 1,
    #             'name': name
    #          }
    #     )
    #     st.success(f'Movie {name} cadastrado com sucesso!')
    #     st.rerun()