from django.views.generic import TemplateView
import requests
from django.conf import settings
from django.shortcuts import render
from accounts.serializers import SmallNBOUserSerializer

class ReactTemplateView(TemplateView):
    app = None
    template_name = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        assets = self._react_render()
        context.update(**assets)
        return context

    def _react_render(self):
        request = self.request
        if request.user.is_authenticated:
            serializer = SmallNBOUserSerializer(request.user)
            user = serializer.data
        else:
            user = {}

        render_assets = {
            'url': '/{}'.format(self.app),
            'props': {
                'user': user,
            }
        }

        try:
            res = requests.post(settings.RENDER_SERVER_BASE_URL + '/render',
                                json=render_assets,
                                headers={'content_type': 'application/json'})
        except Exception as e:
            print (e)

        return res.json()
