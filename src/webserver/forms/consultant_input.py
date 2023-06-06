import streamlit as st
import pandas as pd
from st_clickable_images import clickable_images
from PIL import Image
import time
from streamlit_autorefresh import st_autorefresh
from streamlit_extras.switch_page_button import switch_page


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
                switch_page("Ergebnisabfrage")
                st.experimental_rerun()
                return


def data_form():
    with st.container():
        st.subheader('Consultant Input Data Forms')

        col2, col3 = st.columns(2)
        with col2:

            # 1
            data = st.radio('I\'s your data unstructured or structured ?',
                            ('unstructured', 'structured'), key='value_data')

            accuracy_claim = st.select_slider('What accuracy level you need?',
                                              options=['Low', 'Medium', 'High', 'Very high'], label_visibility='visible', key='value_accuracy_claim')
            dimensions_amount = st.radio('How many features does your data have?', (
                'Medium', 'High', 'Low'), key='value_dimensions_amount')

            data_format = st.radio('In which format is your data?', (
                'Matrix', 'Text', 'Video', 'Image', 'Audio', 'Other'), key='value_data_format')
            data_amount = st.radio('How big is your data volume?', (
                'Very high', 'Low', 'Medium', 'High', 'None'), key='value_data_amount')
            data_quality = st.radio('How would you describe the quality of your data?', (
                'Medium', 'High', 'Very high', 'Low', 'None'), key='value_data_quality')

            data_type = st.radio('How would you describe the type of your data?', (
                'Labeled', 'Mixed', 'Unlabeled', 'Feedback-Signal'), key='value_data_type')
            sequence_of_decisions = st.radio(
                'sequence_of_decisions????', ('Yes', 'No'), key='value_sequence_of_decisions')
            label = st.radio('label???', ('1', '0'), key='value_label')

            computing_power = st.radio('How would you describe the computing power which is available at your company?', (
                'Medium', 'Low', 'High', 'Very high'), key='value_computing_power')
            type_goalsize = st.radio(
                'type_goalsize ???', ('Categorical', 'Numerical', 'None'), key='value_type_goalsize')
            time_availability = st.radio('How urgent do you need the model?', (
                'Medium', 'High', 'Low', 'Very high'), key='value_time_availability')

        if st.button('Submit data', key='button_data'):
            st.balloons()
            st.session_state.feature_input = True
            st.session_state.feature_input_data = {'data': data,
                                                   'accuracy_claim': accuracy_claim,
                                                   'dimensions_amount': dimensions_amount,
                                                   'data_format': data_format,
                                                   'data_amount': data_amount,
                                                   'data_quality': data_quality,
                                                   'data_type': data_type,
                                                   'sequence_of_decisions': sequence_of_decisions,
                                                   'label': label,
                                                   'computing_power': computing_power,
                                                   'type_goalsize': type_goalsize,
                                                   'time_availability': time_availability,
                                                   }
            return
