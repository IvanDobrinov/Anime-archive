from django import template
from django.utils import dateparse
import datetime

register = template.Library()


@register.filter(name='parse_date')
def parse_date(value):
    if isinstance(value, datetime.date):
        return value
    if value:
        return (dateparse.parse_date(value) or dateparse.parse_datetime(value).date())
    return None
