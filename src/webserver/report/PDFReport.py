from report.config import WKHTMLTOPDF_PATH
from datetime import datetime
import jinja2
import pdfkit
import sys
import os


class PDFReport:
    # Class to generate PDF-Report moin

    def __init__(self):
        pass

    def add_img_to_html(self, context_dict):
        relative_path = 'src/webserver/report/assets/IWI-logo.png'
        iwi_logo = self.make_absolute_path(relative_path)
        img_dict = {'iwi_logo': iwi_logo}

        context_dict = self.add_elements_to_dict(context_dict, img_dict)

        return context_dict
    
    def add_fig_to_html(self, context_dict):
        relative_path = 'src/webserver/report/assets/plot.png'
        plot_logo = self.make_absolute_path(relative_path)
        img_dict = {'plot_logo': plot_logo}

        context_dict = self.add_elements_to_dict(context_dict, img_dict)

        return context_dict

    def export_to_pdf(self, html_template, css_style, output_pdf, context_dict):
        # create an environment for the template_loader
        template_loader = jinja2.FileSystemLoader("./")
        template_env = jinja2.Environment(loader=template_loader)

        # Add images to context
        context = self.add_img_to_html(context_dict)
        context = self.add_fig_to_html(context_dict)

        # Read template and write in
        template = template_env.get_template(html_template)
        output_text = template.render(context)

        # Export pdf file
        config = pdfkit.configuration(
            wkhtmltopdf=WKHTMLTOPDF_PATH)
        pdfkit.from_string(output_text, output_pdf, configuration=config,
                           css=css_style, options={"enable-local-file-access": ""})

    def create_report(self, context_dict):
        html_template = 'src/webserver/report/assets/pdf_report.html'
        css_style = 'src/webserver/report/assets/style.css'
        output_pdf = 'src/webserver/report/assets/pdf_report.pdf'

        self.export_to_pdf(html_template, css_style, output_pdf, context_dict)

    def make_absolute_path(self, relative_path):
        # Normiere die Pfade, um sicherzustellen, dass sie die richtige Syntax haben
        relative_path = os.path.normpath(relative_path)
        base_path = os.path.abspath(os.getcwd())

        # Verbinde den relativen Pfad mit dem Basispfad
        absolute_path = os.path.join(base_path, relative_path)

        return absolute_path

    def add_elements_to_dict(self, dictionary, new_elements):
        dictionary.update(new_elements)

        return dictionary
