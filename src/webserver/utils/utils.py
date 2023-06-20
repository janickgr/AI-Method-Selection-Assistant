import streamlit as st
import base64
from PIL import Image
import pandas as pd


def show_pdf(file_path):
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="1200" height="800" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)


def display_session_state():
    if 'selected_profile' not in st.session_state:
        st.session_state['selected_profile'] = False

    if 'company_info' not in st.session_state:
        st.session_state['company_info'] = False

    if 'feature_input' not in st.session_state:
        st.session_state['feature_input'] = False

    if 'company_info_data' not in st.session_state:
        st.session_state['company_info_data'] = {}

    if 'feature_input_data' not in st.session_state:
        st.session_state['feature_input_data'] = {}
        
    if 'output_data' not in st.session_state:
        st.session_state['output_data'] = {}

    if 'tco_clv_data' not in st.session_state:
        st.session_state['tco_clv_data'] = {'tco': None, 'clv': None}

    if st.session_state['selected_profile'] != False:
        st.text('logged in as: {}'.format(
            st.session_state['selected_profile']))


def load_pictures():
    image_user = Image.open('src/webserver/data/user.jpg')
    image_consultant = Image.open('src/webserver/data/consultant.png')
    return image_user, image_consultant


def display_title():
    st.title('AI-Method-Selection-Assistant')

    st.text('Prototype implementation as part of the research study of the Master of Information Systems' +
            '- Digital Transformation at Heilbronn University in 2023.')


# TODO dringend überarbeiten ...
def transform_dummy(data, features):
    for feature in features:
        data[[(str(feature) + '_' + str(col))
              for col in pd.get_dummies(data[feature]).columns]] = pd.get_dummies(data[feature])
        data.drop(feature, axis=1, inplace=True)
    return data


def concat_dummy_user_input(input_data):
    # TODO ganz großer Schmutz
    data_label = {
        'Datenformat_Bild': 0,
        'Datenformat_Keine': 0,
        'Datenformat_Matrix': 0,
        'Datenformat_Text': 0,
        'Datenformat_Ton': 0,
        'Datenformat_Video': 0,      
        'Datenqualität_Gering': 0,
        'Datenqualität_Hoch': 0,
        'Datenqualität_Keine': 0,        
        'Datenqualität_Normal': 0,        
        'Datenqualität_Sehr Hoch': 0,       
        'Verfügbarkeit von Zeit_Gering': 0,
        'Verfügbarkeit von Zeit_Hoch': 0,
        'Verfügbarkeit von Zeit_Normal': 0,
        'Verfügbarkeit von Zeit_Sehr Hoch': 0,      
        'Anspruch auf Genauigkeit_Gering': 0,
        'Anspruch auf Genauigkeit_Hoch': 0,
        'Anspruch auf Genauigkeit_Normal': 0,        
        'Anspruch auf Genauigkeit_Sehr Hoch': 0,       
        'Datentyp_Feedback-Signal': 0,
        'Datentyp_Gelabelt': 0,
        'Datentyp_Gemischt': 0,
        'Datentyp_Nicht gelabelt': 0,       
        'Typ der Zielgröße_Kategorisch': 0,
        'Typ der Zielgröße_Keine': 0,
        'Typ der Zielgröße_Numerisch': 0,      
        'Rechenkapazität_Gering': 0,
        'Rechenkapazität_Hoch': 0,
        'Rechenkapazität_Normal': 0,
        'Rechenkapazität_Sehr Hoch': 0,
        'Datenmenge_Groß': 0,
        'Datenmenge_Keine': 0,
        'Datenmenge_Klein': 0,
        'Datenmenge_Neutral': 0,
        'Datenmenge_Sehr Groß': 0,
        'Folge von Entscheidungen_ja': 0,
        'Folge von Entscheidungen_nein': 0,
        'Anzahl an Dimensionen (Features)_Gering': 0,
        'Anzahl an Dimensionen (Features)_Mittel': 0,
        'Anzahl an Dimensionen (Features)_Hoch': 0
    }

    df_final = pd.DataFrame(data=data_label, index=[0])

    for _, row in input_data.iterrows():
        for col in df_final.columns:
            if col in row.index:
                df_final[col] = 1

    return df_final


def get_clean_methods_names(list) -> list:

    list_methods_names = []

    for entry in list:
        entry = entry.replace("[", "").replace("]", "").replace("'", "")
        entry_list = entry.split(',') 
        list_methods_names.append('{} ({})'.format(entry_list[1],entry_list[3].lstrip(' ')))

    return list_methods_names

