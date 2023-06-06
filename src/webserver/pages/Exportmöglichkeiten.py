import streamlit as st
from streamlit_autorefresh import st_autorefresh
import pandas as pd
import report.main_report
import forms.user_input
import forms.consultant_input
from utils import utils

from datetime import date


# --------------------------------------------------------------------------------

utils.display_title()
utils.display_session_state()

# --------------------------------------------------------------------------------
df_company_data = pd.DataFrame(st.session_state['company_info_data'], index=['0'])
tco = st.session_state['tco_clv_data']['tco']
clv = st.session_state['tco_clv_data']['clv']

output_data = st.session_state['output_data']
company_name = df_company_data.iloc[0][0]
company_street = df_company_data.iloc[0][1]
company_loc = df_company_data.iloc[0][2]
industry = df_company_data.iloc[0][3]
employees = df_company_data.iloc[0][4]  
phone = df_company_data.iloc[0][5]
mail = df_company_data.iloc[0][6]



today = date.today()
formatted_date = today.strftime("%d.%m.%Y")

if st.button('Export PDF-Result'):
    report.main_report.main_report(company_name, company_street, company_loc, formatted_date, phone, mail, tco, clv, output_data)
    utils.show_pdf('src/webserver/report/assets/pdf_report.pdf')

