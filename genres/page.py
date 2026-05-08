import streamlit as st


genres = [
    {
        'id': 1,
        'name': 'Ação'
    },
    {
        'id': 2,
        'name': 'Comédia'
    },
    {
        'id': 3,
        'name': 'Drama'
    }
]

def show_genres():
    st.write("Page genres")

    st.table(genres)

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