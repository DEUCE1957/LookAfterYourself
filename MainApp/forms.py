from django import forms

from django.contrib.auth.models import User
from MainApp.models import UserProfile, Submission, Suggestion


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)

#startYear, startMonth, startDay, startHour, startMinute,
#endYear, endMonth, endDay, endHour, endMinute, description=""
class eventForm(forms.Form):
    name = forms.CharField(label = "Name", max_length=100)
    startDate = forms.DateField(label = "Start date", initial = "dd/mm/yy",input_formats= ['%d/%m/%y'])
    startTime = forms.TimeField(label = "Start time", initial = "hh:mm")
    endDate = forms.DateField(label = "End date", initial = "dd/mm/yy",input_formats= ['%d/%m/%y'])
    endTime = forms.TimeField(label = "End time", initial = "hh:mm")
    description = forms.CharField(label = "Description", max_length=1000,
                                  required = False)
    location= forms.CharField(label = "Location", max_length=256,
                                  required = False)


class SubmitForm(forms.ModelForm):
    title = forms.CharField(max_length=128,
                            help_text="Tip Title:")
    tip = forms.CharField(
        max_length=1000,
        help_text="Tip Content:",
        widget=forms.Textarea
    )

    class Meta:
        model = Submission
        fields = ('title', 'tip')
        exclude = ('tipId',)


class SuggestionForm(forms.ModelForm):
    subject = forms.CharField(max_length=128,
                            help_text="Subject:")
    suggestion = forms.CharField(
        max_length=1000,
        help_text="Suggestion:",
        widget=forms.Textarea
    )

    class Meta:
        model = Suggestion
        fields = ('subject', 'suggestion')
        exclude = ('suggestionId',)
        
        
        
