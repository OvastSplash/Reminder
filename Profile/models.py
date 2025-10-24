from django.db import models
from User.models import User

class Reminder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    remind_at = models.DateTimeField()

    def __str__(self):
        return f"Reminder for {self.user.username} at {self.remind_at}"