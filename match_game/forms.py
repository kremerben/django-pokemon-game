from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from models import *


class GetTeamForm(forms.Form):
    team = forms.ModelChoiceField(queryset=Team.objects.all())

    class Meta:
        model = Team
