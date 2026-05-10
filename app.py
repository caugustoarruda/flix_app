import streamlit as st
from genres.page import show_genres
from actors.page import show_actors
from movies.page import show_movies
from reviews.page import show_reviews
from login.page import show_login


def main():
    if 'token' not in st.session_state:
        show_login()
    else:
        st.title('Flix app')
        
        menu_option = st.sidebar.selectbox(
            'Selecione uma opção: ',
            ['Início', 'Generos', 'Atores', 'Filmes', 'Avaliações']
        )

        if menu_option == 'Início':
            st.write('Inicio')

        elif menu_option == 'Generos':
            show_genres()

        elif menu_option == 'Atores':
            show_actors()

        elif menu_option == 'Filmes':
            show_movies()
            
        else:
            show_reviews()


if __name__ == '__main__':
    main()