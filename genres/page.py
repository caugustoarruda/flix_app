import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
import requests


genres = [
    {
        'id': 1,
        'name': 'Drama'
    }
]
def show_genres():
    st.write("Page genres")
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


    AgGrid(pd.DataFrame(genres))

    st.title('Cadastrar novo genero:')
    name = st.text_input('Nome do genero')
    if st.button('Cadastrar'):
        genres.append(
            {
                'id': len(genres) + 1,
                'name': name
             }
        )
        st.success(f'Genero {name} cadastrado com sucesso!')
        st.rerun()