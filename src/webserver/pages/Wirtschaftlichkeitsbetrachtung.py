import streamlit as st
from streamlit_autorefresh import st_autorefresh

import forms.user_input
import forms.consultant_input
from utils import utils
from models import models
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
    tco = float(initial_investment) + (float(annual_operation_costs) * float(customer_lifetime))
    clv = (float(annual_revenue) * float(customer_lifetime)) - tco
    return tco, clv

if st.button('Berechnen'):
    tco, clv = calculate(initial_investment, annual_operation_costs, annual_revenue, customer_lifetime)
    st.info(f"TCO (Total Cost of Ownership): {tco}")
    st.info(f"CLV (Customer Lifetime Value): {clv}")


