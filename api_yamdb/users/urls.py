from api.views import get_token, signup
from django.urls import path

urlpatterns = [
    path("signup/", signup, name="signup"),
    path("token/", get_token, name="get_token"),
]
