import streamlit as st
import pandas as pd
from st_aggrid import AgGrid


genres = [
    {
        'id': 1,
        'name': 'Drama'
    }
]
def show_genres():
    st.write("Page genres")

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