import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
import requests


actors = [
    {
        'id': 1,
        'name': 'Stallone'
    }
]

def show_actors():
    AgGrid(pd.DataFrame(actors))

    st.title('Cadastrar novo ator:')
    name = st.text_input('Nome do ator')
    if st.button('Cadastrar'):
        actors.append(
            {
                'id': len(actors) + 1,
                'name': name
             }
        )
        st.success(f'Ator {name} cadastrado(a) com sucesso!')
        # st.rerun()