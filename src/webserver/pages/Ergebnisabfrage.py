import streamlit as st
from streamlit_autorefresh import st_autorefresh

import forms.user_input
import forms.consultant_input
from utils import utils

import pandas as pd


# --------------------------------------------------------------------------------

utils.display_title()
utils.display_session_state()

# --------------------------------------------------------------------------------

st.header('TODO....')


df = pd.DataFrame({'data': st.session_state['company_info_data'],
                   'feature_input': st.session_state['feature_input_data']}
                  )

st.write(df)
