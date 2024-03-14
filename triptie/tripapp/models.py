from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models


class UserProfile(models.Model):
    Gender_Choices = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    gender = models.CharField(max_length=1, choices=Gender_Choices, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    bio = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


# table for posting a trip on the app

class TripPlan(models.Model):
    TITLE_MAX_VALUE = 128
    CITY_MAX_VALUE = 32
    DESCRIPTION_MAX_VALUE = 512
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=TITLE_MAX_VALUE)
    description = models.TextField(max_length=DESCRIPTION_MAX_VALUE)
    destination_city = models.CharField(max_length=CITY_MAX_VALUE)
    start_date = models.DateField()
    end_date = models.DateField()
    is_private = models.BooleanField(default=False,blank=True)
    image = models.ImageField(upload_to='trip_images')

    def clean(self):
        # Ensure end_date is after start_date
        if self.end_date < self.start_date:
            raise ValidationError('End date must be after start date.')


# table of giving likes to the post

class LikePost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trip_plan = models.ForeignKey(TripPlan, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


# table for commenting on the post
class Comment(models.Model):
    COMMENT_MAX_VALUE = 128
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trip_plan = models.ForeignKey(TripPlan, on_delete=models.CASCADE)
    comment_content = models.CharField(max_length=COMMENT_MAX_VALUE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']
