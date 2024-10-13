import streamlit as st
import pandas as pd
from utilities import load_dataset

if 'dataframe_fifa' not in st.session_state:
    load_dataset()

st.set_page_config(
    page_title= 'Teams',
    layout= 'wide'
)

df_fifa = st.session_state['dataframe_fifa']

#creating filters
club = st.sidebar.selectbox(label='Select the Club', options=df_fifa['Club'].value_counts().index)

#creating dataset
df_fifa_club = df_fifa[df_fifa['Club'] == club].set_index('Name')

st.image(df_fifa_club.iloc[0]['Club Logo'])
st.markdown(f"## {df_fifa_club.iloc[0]['Club']}")
st.divider()

df_columns_view = ["Age", "Photo", "Flag", "Overall", "Value(£)", "Wage(£)", 'Joined',
                    'Height(cm.)', 'Weight(lbs.)', 'Contract Valid Until', 'Release Clause(£)']

st.dataframe(df_fifa_club[df_columns_view],
                column_config={
                    'Photo' : st.column_config.ImageColumn(label='Player Photo'),
                    'Flag': st.column_config.ImageColumn(label='Player Country'),
                    'Overall': st.column_config.ProgressColumn(min_value=0, max_value=100, format= "%d")
                })