import streamlit as st
import pandas as pd
from utilities import load_dataset


if 'dataframe_fifa' not in st.session_state:
    load_dataset()

st.set_page_config(
    page_title= 'Players',
    layout= 'wide',
    initial_sidebar_state= 'expanded'
)

df_fifa = st.session_state['dataframe_fifa']

#creating filters
club = st.sidebar.selectbox('Select the Club',
                            options= df_fifa['Club'].unique().tolist())

df_fifa_club = df_fifa[df_fifa['Club'] == club]

players = st.sidebar.selectbox('Select the Player',
                               options= df_fifa_club['Name'].value_counts().index)

df_fifa_club_player = df_fifa_club[df_fifa_club['Name'] == players].iloc[0]

#creating page
st.image(df_fifa_club_player['Photo'])
st.title(df_fifa_club_player['Name'])
st.markdown(f"**Club:** {df_fifa_club_player['Club']}")
st.markdown(f"**Position:** {df_fifa_club_player['Position']}")

col1, col2, col3, col4, col5 = st.columns(5)
col1.markdown(f"**Age:** {df_fifa_club_player['Age']}")
col2.markdown(f"**Height:** {df_fifa_club_player['Height(cm.)'] / 100:.2f}")
col3.markdown(f"**Weight :** {df_fifa_club_player['Weight(lbs.)'] * 0.453:.2f}")

st.divider()

st.subheader(f"Overall: {df_fifa_club_player['Overall']}")
st.progress(value=int(df_fifa_club_player['Overall']))

col1, col2, col3 = st.columns(3)
col1.metric(label="Value",value= f"{df_fifa_club_player['Value(£)']:,}")
col2.metric(label="Wage",value= f"{df_fifa_club_player['Wage(£)']:,}")
col3.metric(label="Release Clause",value= f"{df_fifa_club_player['Release Clause(£)']:,}")