from django import forms
from django.forms import widgets
from . import models


class LoginForm(forms.Form):

    email = forms.EmailField(widget=forms.EmailInput(), label="이메일 주소")
    password = forms.CharField(widget=forms.PasswordInput(), label="비밀번호")

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        try:
            user = models.User.objects.get(email=email)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("Password is wrong"))
        except models.User.DoesNotExist:
            self.add_error("email", forms.ValidationError("User does not exist"))


class SignUpForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ("first_name", "gender", "last_name", "email", "birthdate")
        widgets = {
            "first_name": forms.TextInput(attrs={"required": True}),
            "gender": forms.TextInput(attrs={"required": True}),
            "last_name": forms.TextInput(attrs={"required": True}),
            "email": forms.EmailInput(),
            "birthdate": forms.TextInput(
                attrs={"required": True, "class": "datepicker"}
            ),
        }
        date_to = forms.DateField(
            widget=forms.TextInput(
                attrs={"placeholder": "Date to", "class": "datepicker"}
            ),
            required=False,
        )
        labels = {
            "first_name": "이름",
            "gender": "성별",
            "last_name": "닉네임",
            "email": "이메일 주소",
            "birthdate": "생년월일",
        }

    password = forms.CharField(
        widget=forms.PasswordInput(),
        label="비밀번호",
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(),
        label="비밀번호 확인",
    )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            models.User.objects.get(email=email)
            raise forms.ValidationError("That email is already taken")
        except models.User.DoesNotExist:
            return email

    def clean_password1(self):
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")
        if password != password1:
            raise forms.ValidationError("Password confirmation does not match")
        else:
            return password

    def save(self, *args, **kwargs):
        user = super().save(commit=False)
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        user.username = email
        user.set_password(password)
        user.save()
