import sys
sys.path.append('src')

from report.pdf_report import *

def main():
    # Initialise new pdf_report object
    report = PDF_report()

    # Create new dictionary for input context to the report 
    item1 = "Johannes"
    item2 = "Yannik"
    item3 = "Tobi"
    item4 = "Yannik"
    context_dict = {
        'item1': item1,
        'item2': item2,
        'item3': item3,
        'item4': item4
    }
    
    # Create report 
    report.create_report(context_dict)

if __name__== "__main__":
    main()