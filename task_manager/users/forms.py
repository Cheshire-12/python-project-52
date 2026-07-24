from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=False, label=_('First Name'))
    last_name = forms.CharField(max_length=100, required=False, label=_('Last Name'))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'username')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = _('Username')
        self.fields['password1'].label = _('Password')
        self.fields['password2'].label = _('Confirm Password')
             

class CustomUserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100, required=False, label=_('First Name'))
    last_name = forms.CharField(max_length=100, required=False, label=_('Last Name'))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = _('Username')
