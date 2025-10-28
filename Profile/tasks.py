from celery import shared_task
from .models import Reminder
from django.shortcuts import get_object_or_404
from Reminder.settings import TELEGRAM_API_TOKEN
from User.models import User
import requests

@shared_task
def send_reminder(reminder_id):
    try:
        remind = get_object_or_404(Reminder.objects.select_related('user'), id=reminder_id)
        if not remind.user.telegram_id:
            return "User does not have a Telegram ID"
        user = remind.user
        telegram_id = user.telegram_id
        message = remind.message

        url = f"https://api.telegram.org/bot{TELEGRAM_API_TOKEN}/sendMessage"
        payload = {
            "chat_id": telegram_id,
            "text": message
        }

        response = requests.post(url, json=payload)

        if response.status_code == 200:
            print(f"✅ Message sent to {user.username} ({user.telegram_id})")
        else:
            print(f"⚠️ Telegram API error: {response.text}")

    except User.DoesNotExist:
        return "Reminder not found"