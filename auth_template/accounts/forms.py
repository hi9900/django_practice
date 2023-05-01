from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import User

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["nickname"]
        
    def signup(self, request, user):
        # form에 기입된 데이터를 가져오기 위해 cleaned_data
        user.nickname = self.cleaned_data["nickname"]
        user.save()