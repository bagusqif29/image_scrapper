import streamlit as st
import requests
from bs4 import BeautifulSoup

st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display:none;}
    </style>
    """, unsafe_allow_html=True)


st.markdown("<h1 style= 'text-align:center;'>Image HD Scrapper</h1>", unsafe_allow_html=True)

with st.form("Search"):
    keyword = st.text_input("Enter Your Keyword")
    search = st.form_submit_button("Search")

    if search:
        count = 0
        list_link = []
        set_link = set()
        col1, col2 = st.columns(2)
        page = requests.get(f"https://unsplash.com/s/photos/{keyword}")
        soup = BeautifulSoup(page.content, 'lxml')
        rows = soup.find_all("div", class_ = "ripi6")
        for row in rows:
            figures = row.find_all("figure")
            for figure in figures:
                divs = soup.find_all('div', class_='MorZF')

                for div in divs:
                    # Dalam setiap 'div', cari semua elemen 'img'
                    images = div.find_all('img')
                    
                    for img in images:
                        # Dapatkan atribut 'srcset' dari setiap 'img'
                        srcset = img.get('srcset')
                        
                        # Cetak atribut 'srcset' jika ada
                        if srcset is not None and len(set_link) < 36:
                            count+=1
                            srcset_parts = srcset.split(", ")
                            for part in srcset_parts:
                                if '2000w' in part:
                                    # Extract the URL part before ' 1800w'
                                    image_url = part.split(" ")[0]
                                    
                                    set_link.add(image_url)
        
        # st.title(f'Length of list_link: {len(list_link)}')
        
        # st.title(f'Length of ripi6: {len(rows)}')
        # st.title(f'Length of figures: {len(figures)}')
        # st.title(f'Length of morzl: {len(divs)}')
        # st.title(f'Length of image: {len(images)}')
        for a, link in enumerate(set_link):
            if a%2 == 0:
                col1.image(set_link)
            else:
                col2.image(set_link)
                                    
