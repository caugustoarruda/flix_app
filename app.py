import streamlit as st


def main():
    st.title('Flix app')
    
    menu_option = st.sidebar.selectbox(
        'Selecione uma opção: ',
        ['Início', 'Generos', 'Atores', 'Filmes', 'Avaliações']
    )

    if menu_option == 'Início':
        st.write('Inicio')
    elif menu_option == 'Generos':
        st.write('Lista de generos')
    elif menu_option == 'Atores':
        st.write('Lista de Atores')
    elif menu_option == 'Filmes':
        st.write('Lista de Filmes')
    else:
        st.write('Avaliações')


if __name__ == '__main__':
    main()