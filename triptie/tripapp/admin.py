from django.contrib import admin
from tripapp.models import UserProfile, TripPlan, LikePost, Comment

admin.site.register(UserProfile)
admin.site.register(TripPlan)
admin.site.register(LikePost)
admin.site.register(Comment)
