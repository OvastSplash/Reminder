from django.urls import path
from .views import SaveUserId

urlpatterns = [
    path('save/', SaveUserId.as_view(), name="save_telegram_bot")
]
