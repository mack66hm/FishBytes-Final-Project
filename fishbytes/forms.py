from django import forms
from fishbytes.models import Fish
# from users.models import User

# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model=User
#         fields = ('username')




class CatchForm(forms.ModelForm):
    class Meta:
        model = Fish
        fields = ('image', 'name', 'size (inches)', 'weight(lbs)', 'lake', 'date')