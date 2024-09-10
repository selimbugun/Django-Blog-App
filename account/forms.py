from typing import Any
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.forms import ModelForm, widgets
from django.contrib.auth.models import User


from django import forms





class LoginUserForm(AuthenticationForm):
    def __init__(self, request: Any = ..., *args: Any, **kwargs: Any):
        super().__init__(request, *args, **kwargs)
        self.fields['username'].widget = widgets.TextInput(attrs={'class': 'form-control'})
        self.fields['password'].widget = widgets.PasswordInput(attrs={'class': 'form-control'})

    def clean_username(self):
        username = self.cleaned_data.get('username')

        return username
    


class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = widgets.TextInput(attrs={'class': 'form-control'})
        self.fields['email'].widget = widgets.EmailInput(attrs={'class': 'form-control'})
        self.fields['password1'].widget = widgets.PasswordInput(attrs={'class': 'form-control'})
        self.fields['password2'].widget = widgets.PasswordInput(attrs={'class': 'form-control'})


        def clean_email(self):
            email = self.cleaned_data.get('email')

            if User.objects.filter(email = email).exists():
                self.add_error('email', 'Bu email kullanılıyor!')

            return email
        

class UserPasswordChangeForm(PasswordChangeForm):

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

        self.fields["new_password1"].widget = widgets.PasswordInput(attrs={"class": "form-control"})
        self.fields["new_password2"].widget = widgets.PasswordInput(attrs={"class": "form-control"})
        self.fields["old_password"].widget = widgets.PasswordInput(attrs={"class": "form-control"})



class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

        self.fields["first_name"].widget = widgets.TextInput(attrs={"class": "form-control"})
        self.fields["last_name"].widget = widgets.TextInput(attrs={"class": "form-control"})
        self.fields["email"].widget = widgets.EmailInput(attrs={"class": "form-control"})



class UserEmailChangeForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'email']

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

        self.fields["email"].widget = widgets.EmailInput(attrs={"class": "form-control"})
        self.fields["email"].widget = widgets.EmailInput(attrs={"class": "form-control"})



