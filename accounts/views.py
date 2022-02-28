from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

# Create your views here.


def logoutUser(request):
    logout(request)

    return HttpResponseRedirect(reverse("login"))


class Login(View):
    def post(self, request: HttpRequest):
        login_url = request.GET.get("next", reverse("home"))

        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return HttpResponseRedirect(login_url)

        return render(request, "accounts/login.html", context={"form": form})

    def get(self, request: HttpRequest):
        form = AuthenticationForm(data=request.POST)
        return render(request, "accounts/login.html", context={"form": form})


class Register(View):
    def post(self, request: HttpRequest):
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save(True)
            return HttpResponseRedirect(reverse("login"))
        return render(request, "accounts/register.html", context={"form": form})

    def get(self, request):
        form = UserCreationForm()
        return render(request, "accounts/register.html", context={"form": form})
