from streamlit_autorefresh import st_autorefresh
from PIL import Image
import streamlit as st
# from report.PDFReport import PDFReport
import forms.user_input
import forms.consultant_input
# import sys
# sys.path.insert(1, '/src/')


# --------------------------------------------------------------------------------

st.set_page_config(layout='wide')
autorefresh_interval = 2000

if 'selected_profile' not in st.session_state:
    st.session_state['selected_profile'] = False

if 'company_info' not in st.session_state:
    st.session_state['company_info'] = False

if 'feature_input' not in st.session_state:
    st.session_state['feature_input'] = False

st.session_state


if st.button('reset'):
    st.session_state.selected_profile = False
    st.session_state.company_info = False
    st.session_state.feature_input = False

    st.experimental_rerun()

if st.session_state['selected_profile'] != False:
    st.text('logged in as: {}'.format(st.session_state['selected_profile']))

st.write('----')

image_user = Image.open('data/user.jpg')
image_consultant = Image.open('data/consultant.png')

# --------------------------------------------------------------------------------

st.title('AI-Method-Selection-Assistant')

st.text('Prototype implementation as part of the research study of the Master of Information Systems' +
        '- Digital Transformation at Heilbronn University in 2023.')

st.text(
    'Please select the user type for which you want to perform the consultation within the prototype:')

st.write('----')


output_container = st.empty()

if not st.session_state['selected_profile']:
    with output_container:
        with st.container():
            col1, col2 = st.columns(2, gap='small')

            with col1:
                st.image(image_user, width=250)
                if st.button('Start Assistant as a User'):
                    st.session_state.selected_profile = 'user'
                    st.experimental_rerun()

            with col2:
                st.image(image_consultant, width=250)
                if st.button('Start Assistant as a Consultant'):
                    st.session_state.selected_profile = 'consultant'
                    st.experimental_rerun()

    # Erebnis

    # Ausgabe etc.

    # Na dann ....

elif st.session_state['company_info'] and st.session_state['feature_input']:
    with output_container:
        st.text('finished')
        st.success('done')

#    else:

st.write('----')
