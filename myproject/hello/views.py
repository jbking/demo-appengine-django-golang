from django import http
from django.template import RequestContext, Template
from .models import Greeting


def home(request):
    greetings = Greeting.query()
    template = Template('''
{% for greeting in greetings %}
<p class="author">{{ greeting.author }}</p>
<p>{{ greeting.date }}</p>
<pre>{{ greeting.content }}</pre>
{% endfor %}
''')
    return http.HttpResponse(template.render(RequestContext(request, {'greetings': greetings})))
