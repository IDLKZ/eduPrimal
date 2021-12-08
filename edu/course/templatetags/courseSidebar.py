from django import template
from course.models import *

register = template.Library()


@register.simple_tag
def get_course_info():
    return {"category_sidebar": Category.objects.all(), "authors_sidebar": Author.objects.all(),
            "languages_sidebar": Language.objects.all()}

@register.simple_tag
def get_categories():
    return Category.objects.all()


@register.simple_tag(takes_context=True)
def query_transform(context, **kwargs):
    query = context['request'].GET.copy()
    for k, v in kwargs.items():
        query[k] = v
    return query.urlencode()