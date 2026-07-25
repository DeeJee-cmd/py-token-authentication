# write your code here
from django.urls import path

from user.views import (
    CreateUserViewSet,
    CreateTokenView,
    ManageUserView
)

app_name = "user"

urlpatterns = [
    path("register/", CreateUserViewSet, name="register"),
    path("login/", CreateTokenView.as_view(), name="token"),
    path("me/", ManageUserView.as_view(), name="manage")
]
