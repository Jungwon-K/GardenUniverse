import markdown
from django.utils.safestring import mark_safe

def render_markdown(text):
    html = markdown.markdown(
        text,
        extensions=['fenced_code', 'codehilite']
    )
    return mark_safe(html)
