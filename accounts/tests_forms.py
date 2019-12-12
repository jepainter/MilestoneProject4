from django.test import TestCase
from accounts.forms import UserLoginForm, UserRegistrationForm
from accounts.forms import User

class TestUserLoginForm(TestCase):
    """
    Tests for valid User Login form
    """
    def test_cannot_create_form_with_only_username(self):
        form = UserLoginForm({"username": "Test User"})
        self.assertFalse(form.is_valid())
    
    def test_can_create_form_with_all_fields_completed(self):
        form = UserLoginForm({"username": "Test User",
                              "password": "TestPassword"})
        self.assertTrue(form.is_valid())


    
    
    
    
    
    
    