from django import template

register = template.Library()

@register.filter
def add_some_css(field, css):
    """
    li {
    color:#aae9ff;
    }
    """
    return field.as_widget(attrs={"class":css})