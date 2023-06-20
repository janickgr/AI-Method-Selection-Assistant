import streamlit as st
from streamlit_autorefresh import st_autorefresh
from streamlit_extras.switch_page_button import switch_page

import forms.user_input
import forms.consultant_input
import numpy as np
from utils import utils
from results.result_class import Result
import time
import lightgbm as lgb
import matplotlib.pyplot as plt
import pandas as pd
import plotly.tools
import seaborn as sns


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
    
count_methods_output = st.number_input('Anzahl der ausgegebenen KI-Methoden', value=5, key='amount_methods_output')

if st.button('Berechne KI-Methode', key='calculate'):
    input_data = pd.DataFrame(st.session_state['feature_input_data'], index=['0'])
    st.write(input_data)
    input_data = utils.transform_dummy(input_data, input_data.columns)
    final_data = utils.concat_dummy_user_input(input_data)
    st.write(final_data)

    result = Result(final_data, count_methods_output)
    result.create_result_df()
    result.create_result_plot()

    with st.spinner('Verarbeitung und Kalkulation geeigneter KI-Methoden ...'):
        time.sleep(2)
        st.success('Fertig')

        st.session_state.output_data = result.output_df
        
        st.header('Ergebnisse:')
        
        col1, col2, c3 = st.columns(3, gap='small')

        col2.subheader('Übersicht')

        # Verwenden Sie Seaborn, um den Plot zu erstellen

        # Plot im Streamlit anzeigen
        fig, ax = plt.subplots(figsize=(5, 2))
        ax = sns.barplot(data=result.plot_output_df, x=result.plot_output_df["score"], y=result.plot_output_df["name"])
        ax.set_xlabel(' ')  # x-Achsenbeschriftung
        ax.set_ylabel(' ')  # y-Achsenbeschriftung
        st.pyplot(fig)

        fig, ax = plt.subplots()
        ax = sns.barplot(data=result.plot_output_df, x=result.plot_output_df["score"], y=result.plot_output_df["name"])
        ax.set_xlabel(' ')  # x-Achsenbeschriftung
        ax.set_ylabel(' ')  # y-Achsenbeschriftung
        fig = fig.tight_layout()
        fig = ax.get_figure()
        fig.savefig('src/webserver/report/assets/plot.png')

        with st.expander('Weitere Informationen zur Berechnung der Modelle...'):
            st.text('Lorem Ipsum')


        counter = 0

        st.write('----')

        for entry in st.session_state.output_data:

            #TODO utils funktion
            entry = entry.replace("[", "").replace("]", "").replace("'", "")

            entry_list = entry.split(',')

            st.subheader('{}. Platz: \t {}'.format(counter + 1, entry_list[1]))

            col1, col2, c3 = st.columns(3, gap='small')
    
            col1.text('Verfahren:')
            col1.text('Lerntyp: ')
            col1.text('Daten:')


            col2.write(entry_list[2])
            col2.write(entry_list[3])
            col2.write(entry_list[0])

            with st.expander('Weitere Informationen zum Verfahren: {}'.format(entry_list[1])): 
                st.write('Text Text Text')

            st.write('----')

            counter += 1
    

if st.button('Wirtschaftlichkeitsbetrachtung durchführen', key='tco_button'):
    switch_page('Wirtschaftlichkeitsbetrachtung')
