from django import template
from django.urls import resolve

register = template.Library()

@register.inclusion_tag('breadcrumbs.html')
def breadcrumbs(request):
    path = request.path
        # Simple path parsing for breadcrumbs
            parts = path.strip('/').split('/')
                crumbs = []
                    url = ''
                        for part in parts:
                                if part:
                                            url += '/' + part
                                                        crumbs.append({'label': part.capitalize(), 'url': url})
                                                            return {'breadcrumbs': crumbs}