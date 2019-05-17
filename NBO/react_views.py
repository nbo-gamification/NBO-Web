from django.views.generic import TemplateView
import requests
from django.conf import settings
from accounts.serializers import SmallNBOUserSerializer

class ReactTemplateView(TemplateView):
    app = None
    template_name = None

    def get_context_data(self, **kwargs):
        body = self._prepare_body()
        context = super().get_context_data(**kwargs)
        try:
            res = requests.post(settings.RENDER_SERVER_BASE_URL + '/render',
                                json=body,
                                headers={'content_type': 'application/json'})
        except Exception as e:
            context.update(**{'html': '<div>' + str(e) + '</div>'})
            return context

        context.update(**res.json())
        return context

    def _prepare_body(self):
        request = self.request
        if request.user.is_authenticated:
            serializer = SmallNBOUserSerializer(request.user)
            user = serializer.data
        else:
            user = {}

        body = {
            'app': '/{}'.format(self.app),
            'props': {
                'user': user,
            }
        }

        return body
