from django.contrib.auth.models import User
from django.views.generic import ListView
from rest_framework.generics import ListAPIView
from rest_framework.serializers import ModelSerializer, CharField


class UserAccountListView(ListView):
    model = User
    template_name = 'user_account_list.html'
    context_object_name = 'user_accounts'
    queryset = User.objects.all()[:100]

class UserListView(ListAPIView):
    class UserSerializer(ModelSerializer):
        bio = CharField(source='userprofile.bio')

        class Meta:
            model = User
            fields = ['username', 'email', "bio"]

    queryset = User.objects.all()
    serializer_class = UserSerializer
