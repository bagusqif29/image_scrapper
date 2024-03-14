import streamlit as st
import requests
from bs4 import BeautifulSoup


st.set_page_config(layout='wide')
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
        
        set_link = set()
        d_list = [[]]
        link_list = []
        col1, col2, col3, col4 = st.columns(4)
        page = requests.get(f"https://unsplash.com/s/photos/{keyword}")
        soup = BeautifulSoup(page.content, 'lxml')
        rows = soup.find_all("div", class_ = "ripi6")
        for j, row in enumerate(rows):
            temp_list = []
            # st.title('row ke-'+ str(j))
            
            figures = row.find_all("figure")  
            for i in range(len(figures)-1):
                
                # st.title('figure ke-'+ str(i))
                div = figures[i].find("div", class_="MorZF")
                # st.write('morzf =')
                
                img = div.find("img")
                srcset = img['srcset']
                if srcset is not None:
                    srcset_parts = srcset.split(", ")
                    for part in srcset_parts:
                        if '2000w' in part and 'https://plus' not in part:
                            image_url = part.split(" ")[0]
                            # st.write(image_url)
                            set_link.add(image_url)
                            # link_list.append(image_url)
                            # temp_list.append(image_url)
                
                
                
        for a, link in enumerate(set_link):
            if a%4 == 0:
                col1.image(link)
            elif a%4 == 1:
                col2.image(link)
            elif a%4 == 2:
                col3.image(link)
            elif a%4 == 3:
                col4.image(link)    
            else:
                st.write("ERROR")      
