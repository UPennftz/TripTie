from django import forms
from django.contrib.auth.models import User

from tripapp.models import UserProfile, TripPlan, Comment


class TripPlanForm(forms.ModelForm):
    title = forms.CharField(max_length=TripPlan.TITLE_MAX_VALUE, help_text="Please enter the title of the page.")
    start_date = forms.DateField()
    end_date = forms.DateField()
    destination_city = forms.CharField(max_length=TripPlan.CITY_MAX_VALUE,
                                       help_text="Please enter the city of the destination.")
    description = forms.CharField(widget=forms.Textarea, max_length=TripPlan.DESCRIPTION_MAX_VALUE,
                                  help_text="Please enter the description")
    is_private = forms.BooleanField(initial=False)
    image = forms.ImageField(required=False)

    class Meta:
        model = TripPlan
        fields = ['title', 'start_date', 'end_date', 'destination_city', 'description', 'is_private']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)


class UserProfileForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], widget=forms)
    age = forms.IntegerField(min_value=0, max_value=200)
    bio = forms.CharField(widget=forms.Textarea)
    picture = forms.ImageField(required=False)

    class Meta:
        model = UserProfile
        fields = ('gender', 'age', 'picture', 'bio', 'picture')


class CommentForm(forms.ModelForm):
    comment_content = forms.CharField(widget=forms.Textarea, max_length=Comment.COMMENT_MAX_VALUE)

    class Meta:
        model = Comment
