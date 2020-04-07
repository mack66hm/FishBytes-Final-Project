from django import forms
from fishbytes.models import Catch

# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model=User
#         fields = ('username')


class CatchForm(forms.ModelForm):
    size = forms.CharField(label="Size (inches):")
    weight = forms.CharField(label="Weight (lbs):")
    date = forms.DateField(label="Date (MM/DD/YYYY):")
    class Meta:
        model = Catch
        fields = ('image', 'fish', 'size', 'weight', 'lake', 'date', 'longitude', 'latitude',)