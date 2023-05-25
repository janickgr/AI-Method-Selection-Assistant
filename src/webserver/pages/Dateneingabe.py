import streamlit as st
import forms.user_input
import forms.consultant_input


if st.session_state['selected_profile'] == 'user':

    if st.session_state['company_info']:
        forms.user_input.display_user_form()

elif st.session_state['selected_profile'] == 'consultant':

    if not st.session_state['company_info']:
        with st.container():
            forms.consultant_input.company_form()

    if not st.session_state['feature_input']:

        with st.container():
            forms.consultant_input.data_form()
