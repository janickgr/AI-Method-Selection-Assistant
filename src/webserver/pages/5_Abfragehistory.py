import streamlit as st
import time
import pandas as pd

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

def display_history():

    st.subheader('Abfragehistorie')

    query = Query()

    for column_name, column_data in query.query_data.iterrows():
        
        formatted_date = str(column_data[1])
        company_name = str(column_data[2])
        company_street = str(column_data[3])
        company_loc = str(column_data[4])
        industry = str(column_data[5])
        employees = str(column_data[6])
        phone = str(column_data[7])
        mail = str(column_data[8])
        feature_input_data = column_data[9]
  
        with st.expander('Abfrageergebnis der Firma {} vom {}'.format(company_name, formatted_date)):
            #st.write(column_data)
            
            with st.container():    
                
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

                df_input_data = pd.DataFrame(data=eval(feature_input_data), index=[0])
                        
                data_format = df_input_data.iloc[0][0]
                accuracy_claim = df_input_data.iloc[0][1]
                dimensions_amount = df_input_data.iloc[0][2]
                data_amount = df_input_data.iloc[0][3]
                data_quality = df_input_data.iloc[0][4]
                data_type = df_input_data.iloc[0][5]
                sequence_of_decisions = df_input_data.iloc[0][6]
                computing_power = df_input_data.iloc[0][7]
                type_goalsize = df_input_data.iloc[0][8]
                time_availability = df_input_data.iloc[0][9]

                col1, col2, c3 = st.columns(3, gap='small')

                
                col1.subheader('Name: \n')
                
                col1.text('Datenformat')
                col1.text('Anspruch auf Genauigkeit')
                col1.text('Anzahl an Dimensionen (Features)')
                col1.text('Datenmenge')
                col1.text('Datenqualität')
                col1.text('Datentyp')
                col1.text('Folge von Entscheidungen')
                col1.text('Rechenkapazität')
                col1.text('Typ der Zielgröße')
                col1.text('Verfügbarkeit von Zeit')
                
                col2.subheader('Wert: \n')
                col2.text(data_format)
                col2.text(accuracy_claim)
                col2.text(dimensions_amount)
                col2.text(data_amount)
                col2.text(data_quality)
                col2.text(data_type)
                col2.text(sequence_of_decisions)
                col2.text(computing_power)
                col2.text(type_goalsize)  
                col2.text(time_availability)  
                
                st.write('----')

            if st.button('Ergebnisse als PDF Exportieren', key='Button_{}'.format(str(column_data[0]))):
                    #report.main_report.main_report(
                     #company_name, company_street, company_loc, formatted_date, phone, mail, tco, clv, output_data, plot_output_df)
                    with st.spinner('PDF Export wird vorbereitet'):
                        time.sleep(2)
                        utils.show_pdf('src/webserver/report/assets/pdf_report.pdf')

    st.write('----')

    if st.button('Neue Abfrage starten'):
        st.session_state.selected_profile = False
        st.session_state.company_info = False
        st.session_state.feature_input = False
        st.session_state.company_info_data = False
        st.session_state.feature_input_data = False
        st.session_state.output_data = False
        st.session_state.plot_output_data = False
        switch_page('AI_Method_Selection_Assistant')
        
display_history()
            