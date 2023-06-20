import streamlit as st
from streamlit_autorefresh import st_autorefresh
from streamlit_extras.switch_page_button import switch_page

import forms.user_input
import forms.consultant_input
from utils import utils

import time

import pandas as pd


# --------------------------------------------------------------------------------

utils.display_title()
utils.display_session_state()

# --------------------------------------------------------------------------------

st.header('Wirtschaftlichkeitsbetrachtung')

st.subheader('Input:')

col1, col4 = st.columns(2)
with col1:
    initial_investment = st.text_input(
        'Initiales Investment (in EUR):', value='10000', key='initial_investment')
    annual_operation_costs = st.text_input(
        'Jährliche Operationskosten (in EUR):', value='1000', key='annual_operation_costs')
    annual_revenue = st.text_input(
        'Jährlicher Umsatz (in EUR):', value='100000', key='annual_revenue')
    customer_lifetime = st.text_input(
        'Nutzungsdauer der Kunden (in Jahren):', value='3', key='customer_lifetime')


def calculate(initial_investment, annual_operation_costs, annual_revenue, customer_lifetime):
    tco = float(initial_investment) + \
        (float(annual_operation_costs) * float(customer_lifetime))
    clv = (float(annual_revenue) * float(customer_lifetime)) - tco
    st.session_state.tco_clv_data = {'tco': tco, 'clv': clv}
    return tco, clv


if st.button('Berechnen'):
    with st.spinner('Wirtschaftlichkeitsbetrachtung berechnen'):
        tco, clv = calculate(
            initial_investment, annual_operation_costs, annual_revenue, customer_lifetime)

        time.sleep(1)

        col1, col2, c3 = st.columns(3, gap='small')
        col1.subheader('TCO (Total Cost of Ownership):')
        col1.subheader('CLV (Customer Lifetime Value):')

        col2.subheader(str(tco) + ' €')
        col2.subheader(str(clv) + ' €')

if st.button('Exportmöglichkeiten', key='export_button'):
    switch_page('Exportmöglichkeiten')

if st.button('Neu Starten'):
    st.session_state.selected_profile = False
    st.session_state.company_info = False
    st.session_state.feature_input = False
    st.session_state.company_info_data = False
    st.session_state.feature_input_data = False
    st.session_state.output_data = False
    switch_page('AI_Method_Selection_Assistant')
