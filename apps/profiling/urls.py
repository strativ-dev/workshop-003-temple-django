from django.urls import path
from .views import UserAccountListView
from .views import UserListView

urlpatterns = [
    path('accounts/', UserAccountListView.as_view(), name='user_account_list'),
    path('users/', UserListView.as_view(), name='user_list'),
]
