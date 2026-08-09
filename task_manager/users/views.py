from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import ProtectedError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import CustomUserCreationForm, CustomUserUpdateForm

User = get_user_model()


# Mixin to check if the user has permission to modify their own data
class UserPermissionMixin(UserPassesTestMixin):
    def test_func(self):
        return self.get_object() == self.request.user  # type: ignore

    def handle_no_permission(self):
        messages.error(
            self.request,  # type: ignore
            _('You do not have permission to modify another user')
        )
        return redirect('users')


# 1. User List View
class UserListView(ListView):
    model = User
    template_name = 'users/users_list.html'
    context_object_name = 'users'


# 2. Registration of a new user
class UserCreateView(SuccessMessageMixin, CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('login')
    success_message = _('User registered successfully')


# 3. Update user
class UserUpdateView(UserPermissionMixin, SuccessMessageMixin, UpdateView):
    model = User
    form_class = CustomUserUpdateForm
    template_name = 'users/update.html'
    success_url = reverse_lazy('users')
    success_message = _('User updated successfully')


# 4. Delete user
class UserDeleteView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    SuccessMessageMixin,
    DeleteView):
    model = User
    template_name = 'users/delete.html'
    success_url = reverse_lazy('users')
    success_message = _('User deleted successfully')
    
    def test_func(self):
        user = self.get_object()
        return user == self.request.user
    
    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            messages.error(self.request,
                        _('You do not have permission to modify another user.'))
            return redirect('users')
        return super().handle_no_permission()

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except ProtectedError:
            messages.error(
                request,
                _('Cannot delete a user because it is in use')
            )
            return redirect('users')


# 5. Login user
class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('index')
    success_message = _('You are logged in')


# 6. Logout user
class UserLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        messages.info(request, _('You are logged out'))
        return super().dispatch(request, *args, **kwargs)
