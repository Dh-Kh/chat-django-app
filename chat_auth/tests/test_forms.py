from django.test import TestCase
from chat_auth.forms import (RegisterForm, Change_Password,
                             Change_Username, Change_Email)
from django.contrib.auth.models import User
class Test_RegisterForm(TestCase):
    def test_for_register_form(self):
        form = RegisterForm(data = {
            "username": "John",
            "email": "johnlennon@gmail.com",
            "password1": "NewPassword123!",
            "password2": "NewPassword123!",
            })
        self.assertTrue(form.is_valid())
        
        
class Test_Change_Username(TestCase):
    def test_for_change_username(self):
        form = Change_Username(data = {
            "username": "Yoko_and_John"
            })
        self.assertTrue(form.is_valid())
        
class Test_Change_Password(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username = "John", password = "OldPassword4422*")
        
    def test_for_form_change(self):
        form = Change_Password(user=self.user , data = {
            "old_password": 'OldPassword4422*',
            "new_password1": "NewPassword123!",
            "new_password2": "NewPassword123!"
            })
        self.assertTrue(form.is_valid())

class Test_Change_Email(TestCase):
    def test_for_change_email(self):
        form = Change_Email(data = {
            "email": "newJohnLennon@gmail.com"
            })
        self.assertTrue(form.is_valid())
