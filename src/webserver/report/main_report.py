from report.PDFReport import PDFReport
import pandas as pd
import streamlit as st

def main_report(name, street, loc, today, phone, mail, tco, clv, output_data):

    methods_df = pd.read_csv('src/webserver/report/assets/Method_Descriptions.csv', sep=";")

    list_results = []

    for entry in output_data:
        entry = entry.replace("[", "").replace("]", "").replace("'", "")
        entry_list = entry.split(',')
        temp_list = []

        for index, entry in enumerate(entry_list):
            if index == 1:
                entry = entry.lstrip()
            temp_list.append(entry)
        

        if not methods_df.loc[methods_df['Name'] == temp_list[1]].empty:
            row_description_entry = methods_df.loc[methods_df['Name'] == temp_list[1]]
            description = row_description_entry.iloc[0][2]
            advantages = row_description_entry.iloc[0][3]
            disadvantages = row_description_entry.iloc[0][4]
            task_types = row_description_entry.iloc[0][5]

        else:
            description = " <b>tbd:</b> Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet."
            advantages = " <b>tbd:</b> Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet."
            disadvantages = "<b>tbd:</b> Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet."
            task_types = " <b>tbd:</b> Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet."

        temp_list.append(description)   
        temp_list.append(advantages)
        temp_list.append(disadvantages)
        temp_list.append(task_types)
        
        list_results.append(temp_list)

    # Initialise new pdf_report object
    r1 = PDFReport()
    
    context_dict = {
        'name': name,
        'street': street,
        'loc': loc,
        'today': today,
        'phone': phone,
        'mail': mail,
        'tco': tco,
        'clv': clv  
    }

    counter = 0 

    for entry in list_results:
        context_dict['datatype_{}'.format(counter)] = entry[0]
        context_dict['method_{}'.format(counter)] = entry[1]
        context_dict['procedure_{}'.format(counter)] = entry[2]
        context_dict['learntype_{}'.format(counter)] = entry[3] 
        context_dict['description_{}'.format(counter)] = entry[4] 
        context_dict['advantages_{}'.format(counter)] = entry[5]
        context_dict['disadvantages_{}'.format(counter)] = entry[6] 
        context_dict['task_types_{}'.format(counter)] = entry[7] 
        counter += 1

    # Create report
    r1.create_report(context_dict)


if __name__ == "__main__":
    main_report()
