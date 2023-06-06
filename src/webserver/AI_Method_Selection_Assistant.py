from streamlit_autorefresh import st_autorefresh
from streamlit_extras.switch_page_button import switch_page
from PIL import Image
import streamlit as st
from utils import utils


# --------------------------------------------------------------------------------

st.set_page_config(layout='wide')
autorefresh_interval = 2000

# display session state
utils.display_session_state()
image_user, image_consultant = utils.load_pictures()

# --------------------------------------------------------------------------------

utils.display_title()
utils.display_session_state()

# --------------------------------------------------------------------------------

st.subheader(
    'Bitte wählen Sie den Nutzertyp aus, für den Sie die Abfrage innerhalb des Prototyps durchführen möchten:')

output_container = st.empty()

if not st.session_state['selected_profile']:
    with output_container:
        with st.container():
            col1, col2 = st.columns(2, gap='small')

            with col1:
                st.image(image_user, width=250)
                if st.button('Start Assistant as a User', key='profil_user'):
                    st.session_state.selected_profile = 'user'
                    switch_page("Dateneingabe")
                    st.experimental_rerun()

            with col2:
                st.image(image_consultant, width=250)
                if st.button('Start Assistant as a Consultant', key='profil_consultant'):
                    st.session_state.selected_profile = 'consultant'
                    switch_page("Dateneingabe")
                    st.experimental_rerun()

elif st.session_state['company_info'] and st.session_state['feature_input']:
    with output_container:
        st.text('finished')
        st.success('done')

#    else:

st.write('----')

if st.button('reset'):
    st.session_state.selected_profile = False
    st.session_state.company_info = False
    st.session_state.feature_input = False
    st.experimental_rerun()
