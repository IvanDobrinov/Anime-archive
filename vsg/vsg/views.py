from django.http import HttpResponse
from django.template import loader

from .utils import get_base_context


def index(request):
    template = loader.get_template('index.html')
    context = {
        **get_base_context(request),
        'title': 'Welcome!',
    }
    return HttpResponse(
        template.render(context, request)
    )
