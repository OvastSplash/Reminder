from rest_framework import serializers
from User.models import User

class SaveTelegramIdSerializer(serializers.ModelSerializer):
    telegram_id = serializers.CharField(max_length=255)

    class Meta:
        model = User
        fields = ['telegram_id']

    def validate_telegram_id(self, value):
        # Если value — список (QueryDict), возьмём первый элемент
        if isinstance(value, list):
            value = value[0]

        print("validate_telegram_id called")
        
        # Проверка, что ID не чисто числовой (по твоему условию)
        if not value.isdigit():
            raise serializers.ValidationError("Telegram ID must not be purely numeric")

        print("telegram_id is valid")
        return value

    def update(self, user_id, **kwargs):
        telegram_id = self.validated_data.get('telegram_id')  # правильное имя

        if User.objects.filter(telegram_id=telegram_id).exists():
            raise serializers.ValidationError("This Telegram ID is already associated with another user")
            
        user = User.objects.get(id=user_id)
        user.telegram_id = telegram_id
        user.save()
        return user
