import streamlit as st
from streamlit_autorefresh import st_autorefresh

import forms.user_input
import forms.consultant_input
from utils import utils

import pandas as pd


# --------------------------------------------------------------------------------

utils.display_title()
utils.display_session_state()

# --------------------------------------------------------------------------------

st.header('Results')

st.subheader('Company data input:')

with st.expander('Inspect your entered company data input:'):
    df_company_data = pd.DataFrame(
        st.session_state['company_info_data'], index=['0'])

    edited_df = st.experimental_data_editor(df_company_data)

st.subheader('Data input:')

with st.expander('Inspect your entered input data:'):
    df_input_data = pd.DataFrame(
        st.session_state['feature_input_data'], index=['0'])

    edited_df = st.experimental_data_editor(df_input_data)

if st.button('calculate methdod', key='schwanz'):
    st.info('Pantello ist ein Hurensohn')
