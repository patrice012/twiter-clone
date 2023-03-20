from django import template


register = template.Library()

@register.inclusion_tag('auth/partials/dj_form.html', takes_context=True)
def dj_form(context):
    request = context.get('request')
    form = context.get('form')
    
    return {
        'request': request,
        'form':form,
        
    }