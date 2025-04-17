import markdown
import pdfkit
from django.template.loader import render_to_string
from django.core.files.base import ContentFile
from django.utils.safestring import mark_safe

def generate_pdf_from_bio(profile):
    html = render_to_string('blog/cv_template.html', {
        'profile': profile,
    })

    config = pdfkit.configuration(
        wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    )

    options = {
        'enable-local-file-access': None
    }

    try:
        pdf_data = pdfkit.from_string(html, False, configuration=config, options=options)
        profile.cv.save(f"{profile.user.username}_cv.pdf", ContentFile(pdf_data))
    except OSError as e:
        print("[PDFKit Error] wkhtmltopdf failed, but ignoring it because file may still be generated.")
        print(e)

        
def render_markdown(text):
    html = markdown.markdown(
        text,
        extensions=['fenced_code', 'codehilite']
    )
    return mark_safe(html)
