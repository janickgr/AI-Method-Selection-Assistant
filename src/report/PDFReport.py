import jinja2
import pdfkit
from datetime import datetime
from config import WKHTMLTOPDF_PATH

from src.utils import utils


class PDFReport:
    # Class to generate PDF-Report

    def __init__(self):
        # TODO logo
        # TODO text
        pass

    def add_img_to_html(self, context_dict):
        relative_path = 'src/report/assets/hhn-logo.png'
        hhn_logo = utils.Utils.make_absolute_path(relative_path)
        img_dict = {'hhn_logo': hhn_logo}

        context_dict = utils.Utils.add_elements_to_dict(context_dict, img_dict)

        return context_dict

    def export_to_pdf(self, html_template, css_style, output_pdf, context_dict):
        # create an environment for the template_loader
        template_loader = jinja2.FileSystemLoader("./")
        template_env = jinja2.Environment(loader=template_loader)

        # Add images to context
        context = self.add_img_to_html(context_dict)

        # Read template and write in
        template = template_env.get_template(html_template)
        output_text = template.render(context)

        # Export pdf file
        config = pdfkit.configuration(
            wkhtmltopdf=WKHTMLTOPDF_PATH)
        pdfkit.from_string(output_text, output_pdf, configuration=config,
                           css=css_style, options={"enable-local-file-access": ""})

    def create_report(self, context_dict):
        html_template = 'src/report/assets/pdf_report.html'
        css_style = 'src/report/assets/style.css'
        output_pdf = 'src/report/pdf_report.pdf'

        self.export_to_pdf(html_template, css_style, output_pdf, context_dict)
