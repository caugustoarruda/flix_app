import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
import requests


reviews = [
    {
        'id': 1,
        'name': 'Drama'
    }
]
def show_reviews():
    st.write("Page avaliações")
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


    AgGrid(pd.DataFrame(reviews))

    # st.title('Cadastrar novo genero:')
    # name = st.text_input('Nome do rev')
    # if st.button('Cadastrar'):
    #     reviews.append(
    #         {
    #             'id': len(reviews) + 1,
    #             'name': name
    #          }
    #     )
    #     st.success(f'Review {name} cadastrado com sucesso!')
    #     st.rerun()