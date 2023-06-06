import streamlit as st
from streamlit_autorefresh import st_autorefresh
from streamlit_extras.switch_page_button import switch_page

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

st.header('Ergebnisabfrage')

st.subheader('Eingegebene Daten:')

with st.expander('Inspizieren Sie die eingegebenen Daten bezüglich des Unternehmens:'):
    df_company_data = pd.DataFrame(
        st.session_state['company_info_data'], index=['0'])
    
    #st.text('Firmenname: {}'.format(df_company_data['']))
    #st.write(df_company_data[''])


with st.expander('Inspizieren Sie die eingegebenen Daten:'):
    df_input_data = pd.DataFrame(
        st.session_state['feature_input_data'], index=['0'])
    st.write(df_input_data)

if st.button('Berechne KI-Methode', key='calculate'):
    input_data = st.session_state['feature_input_data']
    input_data = utils.transform_dummy(input_data, input_data.columns)
    final_data = utils.concat_dummy_user_input(input_data)
    xgb_model = models.load_model_xgb()

    with st.spinner('Verarbeitung und Kalkulation geeigneter KI-Methoden ...'):
        time.sleep(2)
        st.success('Fertig')

    st.write('Ergebnis:')
    
    st.session_state.output_data = models.xgb_predict(input_data=final_data, xgb_model=xgb_model)
    st.write(st.session_state.output_data)
    

if st.button('Exportmöglichkeiten', key='export_button'):
    switch_page('Exportmöglichkeiten')
