from django import template
from intelligent.views import classify


register = template.Library()

@register.filter
def classify_text(text):
    try:
        label = classify(text)
    except:
        label = ''
    return label