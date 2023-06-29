import streamlit as st
import time
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from streamlit_autorefresh import st_autorefresh
from streamlit_extras.switch_page_button import switch_page

from utils import utils
from results.result_class import Result


# --------------------------------------------------------------------------------

utils.display_title()
utils.display_session_state()

# --------------------------------------------------------------------------------

def display_results():
        
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
        
    count_methods_output = st.number_input('Anzahl der ausgegebenen KI-Methoden', value=10, key='amount_methods_output')

    if st.button('Berechne KI-Methode', key='calculate'):
        input_data = pd.DataFrame(st.session_state['feature_input_data'], index=['0'])
        input_data = utils.transform_dummy(input_data, input_data.columns)
        final_data = utils.concat_dummy_user_input(input_data)

        result = Result(final_data, count_methods_output)
        result.create_result_df()
        result.create_result_plot()

        with st.spinner('Verarbeitung und Kalkulation geeigneter KI-Methoden ...'):
            time.sleep(2)
            col1, col2, c3 = st.columns(3, gap='small')
            col1.success('Berechnung abgeschlossen')

            st.session_state.output_data = result.output_df
            st.session_state.plot_output_data = result.plot_output_df
        
            st.header('Ergebnisse:')
            
            col1, col2, c3 = st.columns(3, gap='small')


            fig = plt.figure(figsize=(10, 4))
            sns.barplot(data=result.plot_output_df, x=result.plot_output_df["score"], y=result.plot_output_df["name"], edgecolor='black', linewidth=1, palette='cool', ci=None)
            plt.xscale("log")
            plt.xlabel("Score")
            plt.ylabel("Methode")
            plt.title("Vergleich der Modelle")
            st.pyplot(fig)

            fig = plt.figure(figsize=(10, 4))
            sns.barplot(data=result.plot_output_df, x=result.plot_output_df["score"], y=result.plot_output_df["name"], edgecolor='black', linewidth=1, palette='cool', ci=None)
            plt.xscale("log")
            plt.xlabel("Score")
            plt.ylabel("Methode")
            plt.title("Vergleich der Modelle")
            fig.tight_layout()
            fig.savefig('src/webserver/report/assets/plot.png')

            counter = 0

            st.write('----')
            
            methods_df = pd.read_csv('src/webserver/report/assets/Method_Descriptions.csv', sep=";")

            for entry in result.output_df:
                    
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

                    if not methods_df.loc[methods_df['Name'] == entry_list[1].lstrip()].empty:
                        row_description_entry = methods_df.loc[methods_df['Name'] == entry_list[1].lstrip()]
                        description = row_description_entry.iloc[0][2]
                        advantages = row_description_entry.iloc[0][3]
                        disadvantages = row_description_entry.iloc[0][4]
                        task_types = row_description_entry.iloc[0][5]
                    else:
                        description = " **tbd:** Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet."
                        advantages = "**tbd:** Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet."
                        disadvantages = "**tbd:** Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet."
                        task_types ="**tbd:** Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet."

                    st.markdown("**Beschreibung:**")
                    st.markdown(description)
                    
                    st.markdown("**Vorteile:**")
                    st.markdown(advantages)

                    st.markdown("**Nachteile:**")
                    st.markdown(disadvantages)

                    st.markdown("**Aufgabentyp:**")
                    st.markdown(task_types)

                st.write('----')

                counter += 1
                
    if st.button('Wirtschaftlichkeitsbetrachtung durchführen', key='tco_button'):
        switch_page('Wirtschaftlichkeitsbetrachtung')

display_results()
