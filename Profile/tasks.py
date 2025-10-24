from celery import shared_task
from .models import Reminder

@shared_task
def send_reminder(reminder_id):
    print("send_reminder task started")
    try:
        reminder = Reminder.objects.get(id=reminder_id)
        print(f"Напоминание для пользователя {reminder.user.username}: {reminder.message} в {reminder.remind_at}")

    except Reminder.DoesNotExist:
        print(f"Напоминание с ID {reminder_id} не найдено")