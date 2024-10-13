import pandas as pd
import pathlib
import streamlit as st
from datetime import datetime

def load_dataset():
    py_cwd = pathlib.Path(__file__)
    dataset_cwd = py_cwd.parent / 'datasets' / 'fifa23_official.csv'

    df_fifa = pd.read_csv(filepath_or_buffer= dataset_cwd, sep= ',', decimal='.', index_col=0)
    df_fifa = df_fifa[df_fifa['Contract Valid Until'] >= datetime.today().year-1]
    df_fifa = df_fifa[df_fifa['Value(£)'] > 0]
    df_fifa = df_fifa.sort_values(by='Overall', ascending=False)

    st.session_state['dataframe_fifa'] = df_fifa