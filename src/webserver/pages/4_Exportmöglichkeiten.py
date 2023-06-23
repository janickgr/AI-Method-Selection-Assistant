import streamlit as st
import pandas as pd
import time

from datetime import date
from streamlit_autorefresh import st_autorefresh
from streamlit_extras.switch_page_button import switch_page

import report.main_report
from history.query import Query
from utils import utils

# --------------------------------------------------------------------------------

utils.display_title()
utils.display_session_state()

# --------------------------------------------------------------------------------

def display_export():
        
    df_company_data = pd.DataFrame(
        st.session_state['company_info_data'], index=['0'])
    tco = st.session_state['tco_clv_data']['tco']
    clv = st.session_state['tco_clv_data']['clv']

    output_data = st.session_state['output_data']
    input_data = st.session_state['feature_input_data']
    plot_output_data = st.session_state['plot_output_data']
    company_name = df_company_data.iloc[0][0]
    company_street = df_company_data.iloc[0][1]
    company_loc = df_company_data.iloc[0][2]
    industry = df_company_data.iloc[0][3]
    employees = df_company_data.iloc[0][4]
    phone = df_company_data.iloc[0][5]
    mail = df_company_data.iloc[0][6]


    today = date.today()
    formatted_date = today.strftime("%d.%m.%Y")

    st.subheader('Feedback zu den Ergebnissen:')

    feedback = st.select_slider('', options=['Überhaupt nicht zufrieden', 'Weniger zufrieden', 'Neutral', 'Zufrieden', 'Sehr zufrieden'], value='Neutral')

    st.write('----')

    if st.button('Ergebnisse abspeichern'):
        query = Query()
        if len(query.query_data) == 0:
            id = 1
        else:
            id = len(query.query_data) + 1 

        data = [id, formatted_date, company_name, company_street, company_loc, industry, employees, str(phone), mail, str(input_data),  str(output_data), feedback, tco, clv, plot_output_data.to_dict(orient='dict')]
        query.save_query_data(data)
        with st.spinner('Abfrage wird abgespeichert'):
            time.sleep(2)
            col1, col2, col3 = st.columns(3, gap='small')
            col1.success('Ergebnisse erfolgreich abgespeichert')

    if st.button('Ergebnisse als PDF Exportieren'):
        report.main_report.main_report(
            company_name, company_street, company_loc, formatted_date, phone, mail, tco, clv, output_data)
        with st.spinner('PDF Export wird vorbereitet'):
            time.sleep(2)
            utils.show_pdf('src/webserver/report/assets/pdf_report.pdf')

display_export()
