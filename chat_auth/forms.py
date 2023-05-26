from django import forms 
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


class RegisterForm(UserCreationForm, forms.Form):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields =  ("username", "email", "password1", "password2")

class Change_Password(PasswordChangeForm):
    verification_field = forms.CharField(required=False)
    class Meta:
        model = User
        fields = []
        
class Change_Username(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username',)
        
class Change_Email(forms.ModelForm):
    verification_field = forms.CharField(required=False)
    class Meta:
        model = User
        fields = ("email",)
        
class CustomUserAdmin(UserAdmin):
    def get_form(self, request, obj = None,**kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        restriction_field = set()
        if not is_superuser:
            restriction_field |= {
                "is_superuser",
                "user_permissions",
                }
        if (not is_superuser
            and obj is not None
            and obj == request.user
                ):
            restriction_field |= {
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
                }
        
        for r in restriction_field:
            if r in form.base_fields:
                form.base_fields[r].disabled = True
        def has_change_permission(self, request, obj=None):
            return False
        def has_delete_permission(self, request, obj=None):
            return False
        return form