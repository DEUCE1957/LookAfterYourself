from django import forms
<<<<<<< HEAD
from django.contrib.auth.models import User
from MainApp.models import UserProfile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)
=======

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
    

    
    
>>>>>>> 3ba0c1092e0a6d5e2829502ffb0fdc08035fffb4
