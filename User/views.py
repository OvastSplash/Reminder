from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from .forms import UserLoginForm, UserRegistrationForm


def index(request):
    return HttpResponse("Добро пожаловать в Reminder!")

class LoginView(View):
    form_class = UserLoginForm

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                print("User logged in:", user.username)
                return redirect('/profile/')

        return render(request, 'User/login.html', {'form': form})

    def get(self, request):
        form = self.form_class()
        return render(request, 'User/login.html', {'form': form})

class RegisterView(View):
    form_class = UserRegistrationForm

    def get(self, request):
        form = self.form_class()
        return render(request, 'User/registration.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')

        return render(request, 'User/registration.html', {'form': form})
