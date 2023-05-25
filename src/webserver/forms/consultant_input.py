import streamlit as st
import pandas as pd
from st_clickable_images import clickable_images
from PIL import Image
import time
from streamlit_autorefresh import st_autorefresh


# --------------------------------------------------------------------------------

def company_form():
    with st.container():
        st.subheader('Consultant Input Organisation Forms')

        col1, col4 = st.columns(2)
        with col1:
            company_name = st.text_input(
                'company name:', value='puma', key='company_name')
            industry = st.text_input(
                'industry:', value='shoes', key='company_name1')
            employees = st.text_input(
                'employees:', value=5, key='company_name2')
            headquarters = st.text_input('headquarters:', value='heilbronn',
                                         key='company_name3')

            if st.button('Submit organisation data', key='button_orga_data'):
                st.session_state.company_info = True
                st.session_state.company_info_data = {'company_name': company_name,
                                                      'industry': industry,
                                                      'employees': employees,
                                                      'headquarters': headquarters}
                st.experimental_rerun()
                return


def data_form():
    with st.container():
        st.subheader('Consultant Input Data Forms')

        col2, col3 = st.columns(2)
        with col2:
            data_type = st.text_input('Welche Daten:', key='company_name123')
            data_amount = st.text_input(
                'Menge an Daten', key='company_name3211231')
            data_task = st.text_input('Aufgabe?', key='company_name1231232')
            data_test = st.text_input('Na dann...:', key='company_name2131233')

        if st.button('Submit data', key='button_data'):
            st.balloons()
            st.session_state.feature_input = True
            st.session_state.feature_input_data = {'data_type': data_type,
                                                   'data_amount': data_amount,
                                                   'data_task': data_task,
                                                   'data_test': data_test}
            return
