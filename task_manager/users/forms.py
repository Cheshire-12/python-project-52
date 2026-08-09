from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=100, required=False, label=_('First Name')
        )
    last_name = forms.CharField(
        max_length=100, required=False, label=_('Last Name')
        )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'username')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = _('Username')
        self.fields['password1'].label = _('Password')
        self.fields['password2'].label = _('Confirm Password')
             

class CustomUserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=100,
        required=False,
        label=_('First Name'),
    )
    last_name = forms.CharField(
        max_length=100,
        required=False,
        label=_('Last Name'),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(),
        required=False,
        label=_('Password'),
        help_text=_('Leave blank if you do not want to change the password'),
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(),
        required=False,
        label=_('Confirm Password'),
        help_text=_('Leave blank if you do not want to change the password'),
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username')
        labels = {
            'username': _('Username'),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password or confirm_password:
            if password != confirm_password:
                self.add_error(
                    'confirm_password',
                    _('Passwords do not match'),
                )

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get('password')

        if password:
            user.set_password(password)

        if commit:
            user.save()
        return user