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
    
#if selected == "Chi sono":
    #st.switch_page("sthome.py")

if selected == "Le mie ricette":
    st.switch_page("ricette")

if selected == "La mia musica":
    st.switch_page("musica")


if st.button("ciao"):
    st.switch_page("ricette")




st.sidebar.write(st.session_state)

col1, col2 = st.columns(2)

col1.image(image_path, use_container_width=True)
col2.markdown("# Benvenuto sul mio blog")
long_text = (
    "Sono Nome del Cuoco, un appassionato di gastronomia e creatore di ricette deliziose." 
    "Qui troverai un angolo dedicato alla scoperta di sapori unici, ingredienti freschi e tecniche culinarie" 
    "che renderanno ogni tuo piatto un'esperienza indimenticabile."
)
col2.markdown(long_text)

st.title("La mia storia")
storia = (
    "La mia avventura culinaria inizia in una piccola cucina di famiglia," 
    "dove i profumi dei piatti tradizionali si mescolavano con le risate e" 
    "le storie raccontate attorno al tavolo. Fin da giovane, ho scoperto che" 
    "la cucina non è solo un modo per nutrirsi, ma un'arte che unisce le persone," 
    "celebra la cultura e racconta storie."
)
st.markdown(storia)
