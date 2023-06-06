from report.PDFReport import PDFReport



def main_report(name, street, loc, today, phone, mail, tco, clv, output_data):
    ########################################################################
    ############################## PDF-REPORT ##############################
    ########################################################################

    # Initialise new pdf_report object
    r1 = PDFReport()

    # Create new dictionary for input context to the report
    context_dict = {
        'name': name,
        'street': street,
        'loc': loc,
        'today': today,
        'phone': phone,
        'mail': mail,
        'tco': tco,
        'clv': clv,
        'output_data': output_data
    }

    # Create report
    r1.create_report(context_dict)


if __name__ == "__main__":
    main_report()
