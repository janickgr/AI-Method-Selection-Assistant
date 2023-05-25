import streamlit as st
import base64
from PIL import Image


def show_pdf(file_path):
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="1200" height="800" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)


def display_session_state():
    if 'selected_profile' not in st.session_state:
        st.session_state['selected_profile'] = False

    if 'company_info' not in st.session_state:
        st.session_state['company_info'] = False

    if 'feature_input' not in st.session_state:
        st.session_state['feature_input'] = False

    if 'company_info_data' not in st.session_state:
        st.session_state['company_info_data'] = []

    if 'feature_input_data' not in st.session_state:
        st.session_state['feature_input_data'] = []

    if st.session_state['selected_profile'] != False:
        st.text('logged in as: {}'.format(
            st.session_state['selected_profile']))


def load_pictures():
    image_user = Image.open('src/webserver/data/user.jpg')
    image_consultant = Image.open('src/webserver/data/consultant.png')
    return image_user, image_consultant


def display_title():
    st.title('AI-Method-Selection-Assistant')

    st.text('Prototype implementation as part of the research study of the Master of Information Systems' +
            '- Digital Transformation at Heilbronn University in 2023.')
