import streamlit as st
import pandas as pd
from st_clickable_images import clickable_images
from PIL import Image
import time
from streamlit_autorefresh import st_autorefresh


# --------------------------------------------------------------------------------


# --------------------------------------------------------------------------------


def display_user_form(state_selected_profile):
    st.text('moin {}'.format(st.session_state['selected_profile']))
    return
