from django.shortcuts import render
from django.views import View


class IndexView(View):
    def get(self, request):
        return render(request, 'tripapp/index.html')


def about(request):
    return render(request, 'tripapp/about.html')


def login(request):
    return render(request, 'tripapp/login.html')


def weather(request):
    return render(request, 'tripapp/weather.html')


def profile(request):
    return render(request, 'tripapp/profile.html')


def myposts(request):
    return render(request, 'tripapp/myposts.html')


def messages(request):
    return render(request, 'tripapp/messages.html')


def explore(request):
    return render(request, 'tripapp/explore.html')
