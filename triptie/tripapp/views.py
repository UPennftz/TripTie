from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View

from tripapp.form import UserProfileForm, TripPlanForm, TripPlanSearchForm
from tripapp.models import UserProfile, TripPlan, LikePost


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
                                'bio': user_profile.bio, })

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
                                'bio': user_profile.bio, })

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


class MyTripPlansView(View):
    @method_decorator(login_required)
    def get(self, request, username):
        trip_plans = TripPlan.objects.filter(user=request.user).order_by('-start_date')

        return render(request, 'tripapp/my_trip_plans.html', {'trip_plans': trip_plans})


class MyLikesView(View):
    @method_decorator(login_required)
    def get(self, request, username):
        liked_trip_plans = LikePost.objects.filter(user=request.user).select_related('trip_plan')

        # Extract the trip plans from the likes
        trip_plans = [like.trip_plan for like in liked_trip_plans]

        context = {
            'trip_plans': trip_plans,
            'user': request.user,
        }

        return render(request, 'tripapp/my_likes.html', context)


class AddPlan(View):
    @method_decorator(login_required)
    def post(self, request, username):
        form = TripPlanForm(request.POST, request.FILES)
        context = {
            'username': username,
        }
        if form.is_valid():
            trip_plan = form.save(commit=False)
            trip_plan.user = request.user
            trip_plan.save()
            return render(request, 'tripapp/success.html')

        context = {
            'form': form,
            'username': username,
        }
        return render(request, 'tripapp/add_plan.html', context)

    @method_decorator(login_required)
    def get(self, request, username):
        context = {
            'username': username,
        }
        return render(request, 'tripapp/add_plan.html', context)


class TripPlanSearch(View):
    @method_decorator(login_required)
    def get(self, request):
        form = TripPlanSearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            # Exclude private trip plans
            trip_plans = TripPlan.objects.filter(title__icontains=query, is_private=False)
            liked_trip_plans = []
            user = request.user
            for trip_plan in trip_plans:
                liked = LikePost.objects.filter(user=user, trip_plan=trip_plan).exists()
                liked_trip_plans.append({'trip_plan': trip_plan, 'liked': liked})
            return render(request, 'tripapp/trip_plan_search.html', {'trip_plans': liked_trip_plans, 'query': query})

        return render(request, 'tripapp/trip_plan_search.html', {'form': form})


class SuccessView(View):
    @method_decorator(login_required)
    def get(self, request):
        return render(request, 'tripapp/success.html')


class AddComment(View):
    @method_decorator(login_required)
    def post(self, request, username):
        return


class AddLike(View):
    @method_decorator(login_required)
    def get(self, request, trip_plan_id):
        trip_plan = TripPlan.objects.get(id=trip_plan_id)
        user = request.user

        # Check if the user has already liked the trip plan
        if LikePost.objects.filter(user=user, trip_plan=trip_plan).exists():
            # User has already liked the trip plan, return an error response
            return JsonResponse({'error': 'User has already liked this trip plan'}, status=400)

        # Like the trip plan
        LikePost.objects.create(user=user, trip_plan=trip_plan)
        return JsonResponse({'success': 'Trip plan liked successfully'})


def user_has_liked_trip_plan(user, trip_plan_id):
    return LikePost.objects.filter(user=user, trip_plan_id=trip_plan_id).exists()


def weather(request):
    return render(request, 'tripapp/weather.html')


def explore(request):
    return render(request, 'tripapp/explore.html')
