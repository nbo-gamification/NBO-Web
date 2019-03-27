from rest_auth.views import LoginView
from accounts.serializers import SmallNBOUserSerializer


class CustomLoginView(LoginView):

    def get_response(self):
        orginal_response = super().get_response()
        serialized_user = SmallNBOUserSerializer().to_representation(self.request.user)
        orginal_response.data.update(**serialized_user)
        return orginal_response
