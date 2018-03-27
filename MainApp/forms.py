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


# Form for users to submit their own tips
class SubmitForm(forms.ModelForm):
    # Initialise fields as charfields with maximum character limits and help text which will display on the page
    title = forms.CharField(max_length=128,
                            help_text="Tip Title:")
    tip = forms.CharField(
        max_length=1000,
        help_text="Tip Content:",
        # Have this charfield display as a text area so there is more room for the user to write and view what they have written
        widget=forms.Textarea
    )

    class Meta:
        # Set the model for the form
        model = Submission
        # Set the fields to be shown on the form
        fields = ('title', 'tip')
        # Set the fields to be hidden as they are assigned automatically
        exclude = ('tipId',)


# Form for users to submit suggestions for the site
class SuggestionForm(forms.ModelForm):
    # Initialise fields as charfields with maximum character limits and help text which will display on the page
    subject = forms.CharField(max_length=128,
                            help_text="Subject:")
    suggestion = forms.CharField(
        max_length=1000,
        help_text="Suggestion:",
        # Have this charfield display as a text area so there is more room for the user to write and view what they have written
        widget=forms.Textarea
    )

    class Meta:
        # Set the model for the form
        model = Suggestion
        # Set the fields to be shown on the form
        fields = ('subject', 'suggestion')
        # Set the fields to be hidden as they are assigned automatically
        exclude = ('suggestionId',)



