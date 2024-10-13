import streamlit as st
import webbrowser
from utilities import load_dataset

load_dataset()

st.set_page_config(
    page_title= 'Home',
    layout='wide',
    initial_sidebar_state= 'expanded'
)

st.markdown('# Dashboard FIFA 2023')
col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
bt_dataset = col1.link_button('Dataset Download', url= 'https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data')
bt_git = col2.link_button('Github Repository', url= 'https://github.com/FeMess?tab=repositories')

st.divider()

st.markdown("""
            This Dashboard was developed utilizing **Python** and two key libraries, they are:

            - **`Pandas`**: to extract, transform and load (ETL) process. 
            - **`Streamlit`**: to create dashboard and deploy it on web. 
            """)

st.sidebar.markdown('Developed by [Felipe Mesquita](https://www.linkedin.com/in/felipemesquita19/)')




