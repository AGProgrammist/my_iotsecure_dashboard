from django import template
from datetime import datetime

register = template.Library()

@register.filter(name='get_age')
def get_age(value):
    """
    This function is generate user's age from their birth
    """
    return datetime.year - value.year

register.filter('get_age', get_age)
