import streamlit as st
from streamlit_option_menu import option_menu
with open('st.css') as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)
image_path = '/Users/piermarone/Desktop/SITOx/pippo.png'


selected = option_menu(
        menu_title = None,
        options=["Chi sono","Le mie ricette","La mia musica"],
        orientation="horizontal",
        default_index=0, 
        icons=['pencil-fill','book','music-note'])
    
if selected == "Chi sono":
    st.switch_page(ricette)

#if selected == "Le mie ricette":
    #st.switch_page("ricette")