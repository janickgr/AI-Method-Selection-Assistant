import streamlit as st
from streamlit_autorefresh import st_autorefresh
from streamlit_extras.switch_page_button import switch_page
import pandas as pd
import report.main_report
from history.query import Query
import forms.user_input
import forms.consultant_input
from utils import utils
import time

from datetime import date


# --------------------------------------------------------------------------------

utils.display_title()
utils.display_session_state()

# --------------------------------------------------------------------------------

st.subheader('Abfragehistorie')

query = Query()

st.write(query.query_data)

for column_name, column_data in query.query_data.iterrows():
    with st.expander('Abfrageergebnis vom: {} der Firma {}'.format(str(column_data[0]), str(column_data[1]))):
        st.write(column_data)
        
        with st.container():
            
            company_name = str(column_data[1])
            company_street = str(column_data[2])
            company_loc = str(column_data[3])
            industry = str(column_data[4])
            employees = str(column_data[5])
            phone = str(column_data[6])
            mail = str(column_data[7])

            col1, col2, c3 = st.columns(3, gap='small')

            col1.subheader('Adresse: \n ')
            col1.text(str(company_name))
            col1.text(str(company_street))
            col1.text(str(company_loc))
            
            col2.subheader('Weitere Informationen: \n')

            col2.text('Branche: ' + str(industry))
            col2.text('Mitarbeiter:  ' + str(employees))
            col2.text('Telefonnummer: ' + str(phone))
            col2.text('E-Mailadresse: ' + str(mail))

            st.write('----')      
            
        # TODO Button identifier muss noch ins dataframe gespeichert werden.    
        if st.button('Ergebnisse als PDF Exportieren', key='Button_{}'.format(str(column_data[0]))):
                #TODO funzt noch nicht in utils schieben bei Export
                # report.main_report.main_report()
                with st.spinner('PDF Export wird vorbereitet'):
                    time.sleep(2)
                    utils.show_pdf('src/webserver/report/assets/pdf_report.pdf')
        
            