from django.urls import path
from .views import LoginView, RegisterView

urlpatterns = [
    path('', LoginView.as_view(), name="login"),
    path('registration/', RegisterView.as_view(), name="register"),
]