import os
import django
import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "triptie.settings")

django.setup()

from django.contrib.auth.models import User
from tripapp.models import UserProfile, TripPlan, LikePost, Comment


def populate():
    # Users
    user_data = [
        {"username": "alice", "password": "alice12345", "email": "alice@example.com"},
        {"username": "bob", "password": "bob12345", "email": "bob@example.com"},
    ]

    users = {}
    for user_info in user_data:
        user = add_user(user_info["username"], user_info["email"], user_info["password"])
        users[user_info["username"]] = user

    # UserProfiles
    user_profiles = [
        {"user": users["alice"], "gender": "F", "age": 28, "bio": "Love traveling."},
        {"user": users["bob"], "gender": "M", "age": 30, "bio": "Enjoy outdoor activities."},
    ]

    for profile in user_profiles:
        add_user_profile(profile["user"], profile["gender"], profile["age"], profile["bio"])

    trip_plans = [
        {"user": users["alice"], "title": "Trip to Paris", "description": "Visiting Louvre",
         "destination_city": "Paris", "start_date": datetime.date(2024, 4, 10), "end_date": datetime.date(2024, 4, 20),
         "is_private": False},
        {"user": users["bob"], "title": "Hiking Adventure", "description": "Exploring the Rockies",
         "destination_city": "Denver", "start_date": datetime.date(2024, 5, 15), "end_date": datetime.date(2024, 5, 25),
         "is_private": True},
        {"user": users["alice"], "title": "Beach Holiday", "description": "Relaxing in Hawaii",
         "destination_city": "Honolulu", "start_date": datetime.date(2024, 6, 5),
         "end_date": datetime.date(2024, 6, 15), "is_private": False},
        {"user": users["bob"], "title": "Exploring Tokyo", "description": "Discovering Japanese culture",
         "destination_city": "Tokyo", "start_date": datetime.date(2024, 7, 20), "end_date": datetime.date(2024, 7, 30),
         "is_private": False},
    ]

    for plan in trip_plans:
        add_trip_plan(plan["user"], plan["title"], plan["description"], plan["destination_city"], plan["start_date"],
                      plan["end_date"], plan["is_private"])

    # Comments
    comments = [
        {"user": users["bob"], "trip_plan": TripPlan.objects.get(title="Trip to Paris"),
         "comment_content": "This sounds like an amazing trip!"},
        {"user": users["alice"], "trip_plan": TripPlan.objects.get(title="Hiking Adventure"),
         "comment_content": "Can't wait to see the photos!"},
    ]

    for comment in comments:
        add_comment(comment["user"], comment["trip_plan"], comment["comment_content"])

    # Likes
    likes = [
        {"user": users["bob"], "trip_plan": TripPlan.objects.get(title="Trip to Paris")},
        {"user": users["alice"], "trip_plan": TripPlan.objects.get(title="Exploring Tokyo")},
    ]

    for like in likes:
        add_like(like["user"], like["trip_plan"])


def add_user(username, email, password):
    user, created = User.objects.get_or_create(username=username, email=email)
    if created:
        user.set_password(password)
        user.save()
    return user


def add_user_profile(user, gender, age, bio):
    profile, created = UserProfile.objects.get_or_create(user=user, gender=gender, age=age, bio=bio)
    if created:
        profile.save()
    return profile


def add_trip_plan(user, title, description, destination_city, start_date, end_date, is_private):
    trip_plan, created = TripPlan.objects.get_or_create(user=user, title=title, description=description,
                                                        destination_city=destination_city, start_date=start_date,
                                                        end_date=end_date, is_private=is_private)
    if created:
        trip_plan.save()
    return trip_plan


def add_comment(user, trip_plan, content):
    comment, created = Comment.objects.get_or_create(user=user, trip_plan=trip_plan, comment_content=content)
    if created:
        comment.save()
    return comment


def add_like(user, trip_plan):
    like, created = LikePost.objects.get_or_create(user=user, trip_plan=trip_plan)
    if created:
        like.save()
    return like


if __name__ == '__main__':
    print("Starting population script...")
    populate()
