from django import template

register = template.Library()

@register.filter
def split(value, arg):
    """Split a string by delimiter. Usage: {{ value|split:"|" }}"""
    if not value:
        return []
    return [x.strip() for x in str(value).split(arg)]

@register.filter
def replace(value, arg):
    """Replace substring. Usage: {{ value|replace:"|,<br>• " }}"""
    if not value:
        return ""
    old, new = arg.split(",", 1) if "," in arg else (arg, "")
    return str(value).replace(old, new)
