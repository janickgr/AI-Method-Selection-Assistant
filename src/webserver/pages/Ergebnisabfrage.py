import streamlit as st
from streamlit_autorefresh import st_autorefresh

import forms.user_input
import forms.consultant_input
from utils import utils
from models import models
import time

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

if st.button('calculate methdod', key='calculate'):
    input_data = st.session_state['feature_input_data']
    input_data = utils.transform_dummy(input_data, input_data.columns)
    final_data = utils.concat_dummy_user_input(input_data)
    xgb_model = models.load_model_xgb()

    with st.spinner('Verarbeitung und Kalkulation geeigneter KI-Methoden ...'):
        time.sleep(2)

    st.write('Ergebnis:')

    st.write(models.xgb_predict(input_data=final_data, xgb_model=xgb_model))
