import streamlit as st
from streamlit_autorefresh import st_autorefresh

import forms.user_input
import forms.consultant_input
from utils import utils

# --------------------------------------------------------------------------------

utils.display_title()
utils.display_session_state()

# --------------------------------------------------------------------------------

if st.button('Export PDF-Result'):
    utils.show_pdf('src/report/pdf_report.pdf')
