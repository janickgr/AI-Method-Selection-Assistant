import streamlit as st
import pandas as pd
from st_clickable_images import clickable_images
from PIL import Image
import time
from streamlit_autorefresh import st_autorefresh
from streamlit_extras.switch_page_button import switch_page
import pandas as pd


# --------------------------------------------------------------------------------

def company_form():
    with st.container():
        st.subheader('Fragenkatalog')

        col1, col4 = st.columns(2)
        with col1:
            company_name = st.text_input(
                'Wie lautet der Name der Firma?', value='IT-Consult Beratungshaus Heilbronn', key='company_name')
            company_street = st.text_input(
                'Wie lautet der Straßenname und die Hausnummer?', value='Stuttgarterstraße 4', key='company_street')
            company_loc = st.text_input(
                'Wie lautet der Ort und die Postleitzahl?', value='74072 Heilbronn', key='company_zip')

            industry = st.text_input(
                'In welcher Branche ist das Unternehmen tätig?', value='Beratung für Mittelstand', key='company_name1')
            employees = st.text_input(
                'Wie viele Mitarbeiter hat das Unternehmen?', value=33, key='company_name2')
            
            phone = st.text_input('Welche Telefonnummer ist für Rückrufe relevant?', value='+49 1512123456', key='phone')
            
            user_mail_input = st.text_input('Welche E-Mail Adresse ist aktuell?', value='thomas.mueller@it-consult.de', key='mail_input')

            st.write('----')

            if st.button('Organisationsdaten übermitteln', key='button_orga_data'):
                st.session_state.company_info = True
                st.session_state.company_info_data = {'company_name': company_name,
                                                      'company_street': company_street,
                                                      'company_loc': company_loc,
                                                      'industry': industry,
                                                      'employees': employees,
                                                      'phone': phone,
                                                      'mail':user_mail_input}
                st.experimental_rerun()


def data_form():
    with st.container():
        st.subheader('Fragenkatalog')

        col2, col3 = st.columns(2)
        with col2:

            data_format = st.radio('Welches Datenformat haben die Daten?', (
                'Bild', 'Text', 'Ton', 'Video', 'Matrix', 'Keine'), key='value_data_format', index=4)

            data_quality = st.radio('Welche Datenqualität besitzen die Daten?', (
                'Sehr Hoch', 'Hoch', 'Mittel', 'Gering', 'Keine'), key='value_data_quality', index=1)

            data_type = st.radio('Welchen Datentyp besitzen die Daten?', (
                'Gelabelt', 'Nicht gelabelt', 'Gemischt', 'Feedback-Signal'), key='value_data_type', index=1)

            data_amount = st.radio('Wie groß ist die Datenmenge?', (
                'Sehr Groß', 'Groß', 'Mittel', 'Klein', 'Keine'), key='value_data_amount', index=1)

            type_goalsize = st.radio('Wie ist der Typ der Zielgröße?', (
                'Numerisch', 'Kategorisch', 'Keine'), key='value_type_goalsize', index=2)

            accuracy_claim = st.select_slider('Welcher Anspruch auf Genauigkeit besteht?',
                                              options=['Gering', 'Normal', 'Hoch', 'Sehr Hoch'], label_visibility='visible', key='value_accuracy_claim', value='Gering')

            dimensions_amount = st.radio('Welche Anzahl an Dimensionen gibt es?', (
                'Hoch', 'Mittel', 'Gering'), key='value_dimensions_amount', index=1)

            sequence_of_decisions = st.radio(
                'Handelt es sich um eine Folge von Entscheidungen?', ('ja', 'nein'), key='value_sequence_of_decisions', index=1)

            computing_power = st.radio('Wie würden sie die vorhanden Rechenkapazität beschreiben?', (
                'Gering', 'Mittel', 'Hoch', 'Sehr Hoch'), key='value_computing_power', index=1)

            time_availability = st.radio('Wie dringend benötigen Sie das Modell?', (
                'Gering', 'Normal', 'Hoch', 'Sehr Hoch'), key='value_time_availability', index=0)

        st.write('----')

        if st.button('Daten übertragen', key='button_data'):
            st.session_state.feature_input = True
            st.session_state.feature_input_data = {'Datenformat': data_format,
                                                    'Anspruch auf Genauigkeit': accuracy_claim,
                                                    'Anzahl an Dimensionen (Features)': dimensions_amount,
                                                    'Datenmenge': data_amount,
                                                    'Datenqualität': data_quality,
                                                    'Datentyp': data_type,
                                                    'Folge von Entscheidungen': sequence_of_decisions,
                                                    'Rechenkapazität': computing_power,
                                                    'Typ der Zielgröße': type_goalsize,
                                                    'Verfügbarkeit von Zeit': time_availability}

            switch_page('Ergebnisabfrage')
            return
