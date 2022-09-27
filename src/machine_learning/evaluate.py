import streamlit as st
import pandas as pd
from src.data_management import load_pickle_file

def load_test_evaluation(version):
    st.dataframe(pd.DataFrame(
        load_pickle_file(f'outputs/{version}/evaluation.pk1'), index=['Loss', 'Accuracy']))