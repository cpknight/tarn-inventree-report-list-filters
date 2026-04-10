"""Custom template filters for InvenTree report/label templates.

Filters use a 'tarn_' prefix to avoid name collisions with Python string
methods (str.split, str.replace) which can confuse Django's template
resolution, especially inside {% for %} tags.

These filters are registered against InvenTree's built-in 'report' template
library in apps.py ready(), so they are available via {% load report %}.

They are also available via {% load list_filters %} as a standalone library.
"""

import logging

from django import template

register = template.Library()
logger = logging.getLogger("inventree")


@register.filter(name="tarn_split")
def tarn_split(value, arg):
    """Split a string by delimiter.

    Usage: {{ value|tarn_split:"|" }}
    Returns a list of stripped strings, or an empty list on failure.
    """
    try:
        if not value:
            return []
        return [x.strip() for x in str(value).split(str(arg))]
    except Exception as e:
        logger.warning("tarn_split filter error: %s", e)
        return []


@register.filter(name="tarn_replace")
def tarn_replace(value, arg):
    """Replace a substring. The argument uses a comma to separate old,new.

    Usage: {{ value|tarn_replace:"|,<br>\u2022 " }}
    Returns the original value unchanged on failure.
    """
    try:
        if not value:
            return ""
        old, new = str(arg).split(",", 1) if "," in str(arg) else (str(arg), "")
        return str(value).replace(old, new)
    except Exception as e:
        logger.warning("tarn_replace filter error: %s", e)
        return str(value) if value else ""
