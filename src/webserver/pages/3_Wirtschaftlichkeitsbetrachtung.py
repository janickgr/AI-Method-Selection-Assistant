import streamlit as st
import time
import pandas as pd


from streamlit_autorefresh import st_autorefresh
from streamlit_extras.switch_page_button import switch_page

import forms.consultant_input
from utils import utils

# --------------------------------------------------------------------------------

utils.display_title()
utils.display_session_state()

# --------------------------------------------------------------------------------

def display_economic_calculation():
    
    tco = 20499.0
    clv = 7479501.0 

    st.header('Wirtschaftlichkeitsbetrachtung')

    col1, col4 = st.columns(2)
    with col1:
        initial_investment = st.text_input(
            'Initiales Investment (in EUR):', value='7999', key='initial_investment')
        annual_operation_costs = st.text_input(
            'Jährliche Operationskosten (in EUR):', value='2500', key='annual_operation_costs')
        annual_revenue = st.text_input(
            'Jährlicher Umsatz (in EUR):', value='1500000', key='annual_revenue')
        customer_lifetime = st.text_input(
            'Nutzungsdauer der Kunden (in Jahren):', value='5', key='customer_lifetime')

    if st.button('Berechnen'):
        with st.spinner('Wirtschaftlichkeitsbetrachtung berechnen'):
            
            tco = float(initial_investment) + \
            (float(annual_operation_costs) * float(customer_lifetime))
            
            clv = (float(annual_revenue) * float(customer_lifetime)) - tco

            time.sleep(1)
            col1.success('Berechnung abgeschlossen')

            col1, col2, c3 = st.columns(3, gap='small')
            col1.subheader('TCO (Total Cost of Ownership):')
            col1.subheader('CLV (Customer Lifetime Value):')

            col2.subheader(str(tco) + ' €')
            col2.subheader(str(clv) + ' €')

            st.session_state.clv = clv
            st.session_state.tco = tco

    st.write('----')

    if st.button('Exportmöglichkeiten', key='export_button'):
        switch_page('Exportmöglichkeiten')

display_economic_calculation()
