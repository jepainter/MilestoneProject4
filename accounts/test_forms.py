from django.test import TestCase
from accounts.forms import (
    UserLoginForm, 
    UserRegistrationForm,
    ProfileUpdateForm
    )
from accounts.forms import User

class TestUserLoginForm(TestCase):
    """
    Tests for valid User Login forms
    """
    def test_cannot_create_form_with_only_username_with_messages(self):
        form = UserLoginForm({
            "username": "TestUser1",
            "password": ""
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors["password"],
            ['This field is required.']
        )
    
    def test_can_create_form_with_all_fields_completed(self):
        form = UserLoginForm({
            "username": "Test User1",
            "password": "TestPassword1"
        })
        self.assertTrue(form.is_valid())


class TestUserRegistrationForm(TestCase):
    """
    Tests for valid User Registration forms
    """
    def test_cannot_create_form_with_only_username_with_messages(self):
        form = UserRegistrationForm({
            "username": "TestUser2",
            "email": "",
            "password1": "",
            "password2": ""
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors["email"],
            ["This field is required."]
        )
        self.assertEqual(
            form.errors['password1'],
            ['This field is required.']
        )
        self.assertEqual(
            form.errors['password2'],
            ['This field is required.']
        )
    
    def test_can_create_form_with_all_fields_completed(self):
        form = UserRegistrationForm({
            "username": "TestUser2",
            "email" : "test@example.com",
            "password1": "TestPassword2",
            "password2": "TestPassword2",
        })
        self.assertTrue(form.is_valid())
    
    def test_cannot_create_user_with_mismatched_passwords_with_messages(self):
        form = UserRegistrationForm({
            "username": "TestUser2",
            "email" : "test@example.com",
            "password1": "TestPassword1",
            "password2": "TestPassword2",
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['password2'],
            ['Your passwords do not match.']
        )
        
    def test_cannot_create_user_with_invalid_email_with_messages(self):
        form = UserRegistrationForm({
            "username": "TestUser2",
            "email" : "test",
            "password1": "TestPassword2",
            "password2": "TestPassword2",
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['email'],
            ['Enter a valid email address.']
        )

    
class TestProfileUpdateForm(TestCase):
    """
    Tests for valid User Profile Update forms
    """
    def test_cannot_create_form_with_only_username_with_messages(self):
        form = UserRegistrationForm({
            "username": "Test User3",
            "email": ""
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors["email"],
            ["This field is required."]
        )
    
    def test_can_create_form_with_all_fields_completed(self):
        form = UserRegistrationForm({
            "username": "Test User3",
            "email" : "test3@example.com",
        })
        self.assertFalse(form.is_valid())
    
    def test_cannot_update_user_with_invalid_email_with_messages(self):
        form = UserRegistrationForm({
            "username": "Test User3",
            "email" : "test",
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['email'],
            ['Enter a valid email address.']
        )
    
    
    
    