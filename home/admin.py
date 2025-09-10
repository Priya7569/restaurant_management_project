# templatetags/breadcrumbs.py
from django import template
register = template.Library()

@register.inclusion_tag('breadcrumbs.html')
def breadcrumbs(request):
    path = request.path.strip('/').split('/')
        crumbs = []
            url = ''
                for item in path:
                        url += f'/{item}'
                                crumbs.append({'label': item.capitalize(), 'url': url})
                                    return {'crumbs': crumbs}