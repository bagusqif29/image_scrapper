import streamlit as st
import requests
from bs4 import BeautifulSoup

st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    .stDeployButton {display:none;}
    </style>
    """, unsafe_allow_html=True)


st.markdown("<h1 style= 'text-align:center;'>Web Scrapper</h1>", unsafe_allow_html=True)

with st.form("Search"):
    keyword = st.text_input("Enter Your Keyword")
    search = st.form_submit_button("Search")

    if search:
        count = 0
        list_link = []
        col1, col2 = st.columns(2)
        page = requests.get(f"https://unsplash.com/s/photos/{keyword}")
        soup = BeautifulSoup(page.content, 'lxml')
        rows = soup.find_all("div", class_ = "ripi6")
        for row in rows:
            figures = row.find_all("figure")
            for i in range(2):
                divs = soup.find_all('div', class_='MorZF')

                for div in divs:
                    # Dalam setiap 'div', cari semua elemen 'img'
                    images = div.find_all('img')
                    
                    for img in images:
                        # Dapatkan atribut 'srcset' dari setiap 'img'
                        srcset = img.get('srcset')
                        
                        # Cetak atribut 'srcset' jika ada
                        if srcset is not None and count < 35:
                            count+=1
                            srcset_parts = srcset.split(", ")
                            for part in srcset_parts:
                                if '2000w' in part:
                                    # Extract the URL part before ' 1800w'
                                    image_url = part.split(" ")[0]
                                    
                                    list_link.append(image_url)
        
        # st.title(f'Length of list_link: {len(list_link)}')
        for a in range(len(list_link)):
            if a%2 == 0:
                col1.image(list_link[a])
            else:
                col2.image(list_link[a])
                                    
