from django.shortcuts import render
from django.views import View
from .forms import ProfileForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .tasks import send_reminder

# Create your views here.
@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    form_class = ProfileForm

    def get(self, request):
        form = self.form_class()
        return render(request, 'Profile/profile.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            remind_message = form.save(commit=False)
            remind_message.user = request.user
            remind_message.save()

            send_reminder.apply_async((remind_message.id, ), eta=remind_message.remind_at)

            return render(request, 'Profile/profile.html', {'form': form})

        return render(request, 'Profile/profile.html', {'form': form})

