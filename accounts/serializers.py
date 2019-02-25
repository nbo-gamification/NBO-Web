from rest_auth.serializers import UserDetailsSerializer

from accounts.models import NBOUser


class SmallNBOUserSerializer(UserDetailsSerializer):

    class Meta:
        model = NBOUser
        fields = ('pk', 'email', 'first_name', 'last_name')
        read_only_fields = ('pk', 'email', 'first_name', 'last_name', )
