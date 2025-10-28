from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import SaveTelegramIdSerializer
from User.models import User

class SaveUserId(APIView):
    def post(self, request, *args, **kwargs):
        print(request.data)  # для отладки

        serializer = SaveTelegramIdSerializer(data=request.data)
        if serializer.is_valid():
            serializer.update(user_id=request.data.get("user_id"))
            return Response({"message": "Telegram ID saved successfully"}, status=200)

        print(serializer.errors)  # покажет, почему не проходит валидация
        return Response({"message": "Info is not correct", "errors": serializer.errors}, status=400)
