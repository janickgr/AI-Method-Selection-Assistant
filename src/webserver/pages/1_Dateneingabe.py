import streamlit as st

from streamlit_autorefresh import st_autorefresh

import forms.user_input
import forms.consultant_input
from utils import utils

# --------------------------------------------------------------------------------

utils.display_title()
utils.display_session_state()

# --------------------------------------------------------------------------------

output_container = st.empty()

def display_input():
    if st.session_state['selected_profile'] == 'user':
        if not st.session_state['company_info']:
            with output_container:
                forms.consultant_input.company_form()

        if not st.session_state['feature_input'] and st.session_state['company_info'] == True:
            with output_container:
                forms.consultant_input.data_form()
                
    elif st.session_state['selected_profile'] == 'consultant':
        if not st.session_state['company_info']:
            with output_container:
                forms.consultant_input.company_form()

        if not st.session_state['feature_input'] and st.session_state['company_info'] == True:
            with output_container:
                forms.consultant_input.data_form()

    else:
        st.error('Please select a User role ...')

# --------------------------------------------------------------------------------

display_input()
