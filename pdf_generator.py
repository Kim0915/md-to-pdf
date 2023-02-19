import os
import json
import re

import markdown
from xhtml2pdf import pisa

from pygments.formatters import HtmlFormatter

from markdown.extensions.codehilite import CodeHiliteExtension
from markdown.extensions.tables import TableExtension

class CustomHtmlFormatter(HtmlFormatter):
    def __init__(self, lang_str='', **options):
        super().__init__(**options)
        # lang_str has the value {lang_prefix}{lang}
        # specified by the CodeHilite's options
        self.lang_str = lang_str

    def _wrap_code(self, source):
        yield 0, f'<code class="{self.lang_str}">'
        yield from source
        yield 0, '</code>'

# Get all Directories in current folder
valid_directories = os.listdir(os.path.join(os.curdir, "Markdown Files"))
print(valid_directories)




def convert_html_to_pdf(source_html, output_filename):
    result_file = open(output_filename, "w+b")
    css_path = os.path.join(os.curdir, "style.css")

    css_file = open(css_path, encoding="utf-8")
    pisa_status = pisa.CreatePDF(
        source_html,
        dest=result_file,
        default_css=css_file.read()
    )
    css_file.close()

    result_file.close()
    return pisa_status.err


def create_dir(folder_name, parent_path):
    path = os.path.join(parent_path, folder_name)
    os.mkdir(path)
    return path

# Create PDF Folder
if os.path.isdir(os.path.join(os.curdir, "PDF")):
    PDF_path = os.path.join(os.curdir, "PDF")
else:
    PDF_path = create_dir("PDF", os.curdir)

# for each valid directories look at config.json first

for files in valid_directories:
    print(files)
    md_path = os.path.join("Markdown Files", files)
    print(md_path)
    # If it is not a markdown file ignore it
    if (not md_path.endswith('.md')):
        continue

    # Read the markdown file and create html
    f = open(md_path, encoding="utf-8")
    file_content = "<img align='left' src='https://lh4.googleusercontent.com/zlZaPKBO8pOKv1uQ6VE29IcLjJM4fhQI3ZmkiD-esCoBOT-JHYl27Msjplm5BbHxKvxv0OnVI26InECM710_j-gGEI4tJoQ0yi4MJ-xxhrTEzxupoW5k-Ju3o4OFotj8LXoGCMMOZZPNL5I2Yiqq5Q' alt='logo' width='100' margin='0;0;0' \/>\n"
    file_content = file_content + f.read()

    html = markdown.markdown(file_content, extensions=['fenced_code', 'nl2br', TableExtension(use_align_attribute=True), 'mdx_linkify', CodeHiliteExtension(pygments_formatter=CustomHtmlFormatter)])
    # print(html)
    # Create PDF using HTML
    output_filename = str(files).replace(".md", ".pdf")
    pdf_file_location = os.path.join(PDF_path, output_filename)
    convert_html_to_pdf(html, pdf_file_location)
    f.close()

