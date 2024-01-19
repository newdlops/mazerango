from django import template

register = template.Library()

@register.filter
def mazerango_class(field, css_class):
    attr = field.field.widget.attrs
    widget = field.field.widget
    if hasattr(widget, 'input_type') and widget.input_type == 'select':
        field.field.widget.template_name = 'mazerango/widgets/select.html'
        return field
    if 'class' in attr:
        return field.as_widget(attrs={"class": f"{css_class} {attr['class']}"})
    return field.as_widget(attrs={"class": css_class})


@register.filter
def mazerango_checkbox(field):
    return field.as_widget(attrs={"class": "form-check-input"})
