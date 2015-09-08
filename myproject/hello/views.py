from django import http
from django.template import RequestContext, Template
from .models import Greeting, User


def home(request):
    greetings = Greeting.objects.all()
    template = Template('''
{% for greeting in greetings %}
<p class="author">{{ greeting.author }}</p>
<p>{{ greeting.date }}</p>
<pre>{{ greeting.content }}</pre>
{% endfor %}
''')
    return http.HttpResponse(template.render(RequestContext(request, {'greetings': greetings})))


def create_super_user(request):
    u = User()
    u.username = 'yusuke'
    u.email = 'yusuke@jbking.org'
    u.set_password('hopstep')
    u.is_superuser = True
    u.is_staff = True
    u.is_active = True
    u.save()
    return http.HttpResponse('created')
