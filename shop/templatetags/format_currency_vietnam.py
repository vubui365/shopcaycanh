import locale

from django import template

register = template.Library()

def format_currency_vietnam(number):
    locale.setlocale(locale.LC_ALL, 'vi_VN')

    formatted_number = locale.format_string("%d", number, grouping=True)  + "đ"

    return formatted_number

register.filter('format_currency_vietnam', format_currency_vietnam)
