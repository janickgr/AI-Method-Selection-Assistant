import streamlit as st
from streamlit_autorefresh import st_autorefresh
from streamlit_extras.switch_page_button import switch_page

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

st.header('Ergebnisabfrage')

st.subheader('Eingegebene Daten:')

with st.container():
    df_company_data = pd.DataFrame(
    st.session_state['company_info_data'], index=['0'])

    company_name = df_company_data.iloc[0][0]
    company_street = df_company_data.iloc[0][1]
    company_loc = df_company_data.iloc[0][2]
    industry = df_company_data.iloc[0][3]
    employees = df_company_data.iloc[0][4]
    phone = df_company_data.iloc[0][5]
    mail = df_company_data.iloc[0][6]

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

with st.container():
    
    df_input_data = pd.DataFrame(
        st.session_state['feature_input_data'], index=['0'])
            
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
    

if st.button('Berechne KI-Methode', key='calculate'):
    input_data = pd.DataFrame(st.session_state['feature_input_data'], index=['0'])
    input_data = utils.transform_dummy(input_data, input_data.columns)
    final_data = utils.concat_dummy_user_input(input_data)
    xgb_model = models.load_model_xgb()

    with st.spinner('Verarbeitung und Kalkulation geeigneter KI-Methoden ...'):
        time.sleep(2)
        st.success('Fertig')

    st.write('Ergebnis:')
    
    st.session_state.output_data = models.xgb_predict(input_data=final_data, xgb_model=xgb_model)
    st.write(st.session_state.output_data)

if st.button('Wirtschaftlichkeitsbetrachtung durchführen', key='tco_button'):
    switch_page('Wirtschaftlichkeitsbetrachtung')
