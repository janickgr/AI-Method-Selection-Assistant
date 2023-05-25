from PDFReport import PDFReport

def main_report():
    ########################################################################
    ############################## PDF-REPORT ##############################
    ########################################################################

    # Initialise new pdf_report object
    report = PDFReport()

    # Create new dictionary for input context to the report
    item1 = "Johannes na dann ..."
    item2 = "Yannik"
    item3 = "Tobi aka der Coder"
    item4 = "Janick"
    context_dict = {
        'item1': item1,
        'item2': item2,
        'item3': item3,
        'item4': item4
    }

    # Create report
    report.create_report(context_dict)


if __name__ == "__main__":
    main_report()
