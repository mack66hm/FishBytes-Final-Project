from django import forms
from fishbytes.models import Catch

# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model=User
#         fields = ('username')


class CatchForm(forms.ModelForm):
    class Meta:
        model = Catch
        fields = ('image', 'fish', 'size', 'weight', 'lake', 'date', 'longitude', 'latitude',)