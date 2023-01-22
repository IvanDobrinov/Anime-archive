from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError
from django.forms import forms, PasswordInput
from django.forms.fields import EmailField, CharField
from django.contrib.auth.models import User


class NewUserForm(UserCreationForm):
    email = EmailField(required=True)

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class ChangeUserForm(UserChangeForm):
    email = EmailField(required=True)
    first_name = CharField(required=False)
    last_name = CharField(required=False)
    password = None
    new_password1 = CharField(
        label="Password",
        strip=False,
        widget=PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
        required=False,
    )
    new_password2 = CharField(
        label="Password confirmation",
        widget=PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text="Enter the same password as before, for verification.",
        required=False,
    )
    error_messages = {
        "password_mismatch": "The two password fields didn’t match.",
    }

    def clean_password2(self):
        password1 = self.cleaned_data.get("new_password1")
        password2 = self.cleaned_data.get("new_password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                self.error_messages["password_mismatch"],
                code="password_mismatch",
            )
        return password2

    def _post_clean(self):
        super()._post_clean()
        # Validate the password after self.instance is updated with form data
        # by super().
        password = self.cleaned_data.get("new_password2")
        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except ValidationError as error:
                self.add_error("new_password2", error)

    def save(self, commit=True):
        user = super(ChangeUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if self.cleaned_data["new_password1"]:
            user.set_password(self.cleaned_data["new_password1"])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'new_password1', 'new_password2')
