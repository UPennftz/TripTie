from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View

from tripapp.form import UserProfileForm
from tripapp.models import UserProfile


class IndexView(View):
    def get(self, request):
        return render(request, 'tripapp/index.html')


class AboutView(View):
    def get(self, request):
        return render(request, 'tripapp/about.html')


class ProfileView(View):
    def get_user_details(self, username):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return None

        user_profile = UserProfile.objects.get_or_create(user=user)[0]
        form = UserProfileForm({'gender': user_profile.gender,
                                'picture': user_profile.picture,
                                'bio': user_profile.bio,})

        return user, user_profile, form

    @method_decorator(login_required)
    def get(self, request, username):
        try:
            (user, user_profile, form) = self.get_user_details(username)
        except TypeError:
            return redirect(reverse('tripapp:index'))

        context_dict = {'user_profile': user_profile,
                        'selected_user': user,
                        'form': form}

        return render(request, 'tripapp/profile.html', context_dict)


class EditProfileView(View):

    @method_decorator(login_required)
    def get(self, request, username):
        try:
            (user, user_profile, form) = self.get_user_details(username)
        except TypeError:
            return redirect(reverse('tripapp:index'))

        context_dict = {'user_profile': user_profile,
                        'selected_user': user,
                        'form': form}

        return render(request, 'tripapp/edit_profile.html', context_dict)
    def get_user_details(self, username):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return None

        user_profile = UserProfile.objects.get_or_create(user=user)[0]
        form = UserProfileForm({'gender': user_profile.gender,
                                'picture': user_profile.picture,
                                'bio': user_profile.bio,})

        return user, user_profile, form

    @method_decorator(login_required)
    def post(self, request, username):
        try:
            (user, user_profile, form) = self.get_user_details(username)
        except TypeError:
            return redirect(reverse('tripapp:index'))

        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)

        if form.is_valid():
            form.save(commit=True)
            return redirect(reverse('tripapp:profile',
                                    kwargs={'username': username}))
        else:
            print(form.errors)

        context_dict = {'user_profile': user_profile,
                        'selected_user': user,
                        'form': form}

        return render(request, 'tripapp/edit_profile.html', context_dict)


def weather(request):
    return render(request, 'tripapp/weather.html')


def myposts(request):
    return render(request, 'tripapp/myposts.html')


def messages(request):
    return render(request, 'tripapp/messages.html')


def explore(request):
    return render(request, 'tripapp/explore.html')
