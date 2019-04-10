from django.contrib.auth.views import LoginView
from accounts.forms import Loginform
from django.shortcuts import render
import json

class ReactUserLoginView(LoginView):
    form_class = Loginform
    template_name = 'react/login.html'
    title = 'Login'
    template = 'react/login.html'
    component = 'components/login.js'

    def get(self, request):
        # gets passed to react via window.props
        props = {
            'users': [
                {'username': 'alice'},
                {'username': 'bob'},
            ]
        }

        context = {
            'title': self.title,
            'component': self.component,
            'props': json.dumps(props),
        }

        return render(request, self.template, context)
