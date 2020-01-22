from django.test import TestCase
from histories.forms import HistoryEventForm

class TestHistoryEventForm(TestCase):
    """
    Tests for valid History Event forms
    """
    def test_cannot_create_form_with_missing_fields_with_messages(self):
        form = HistoryEventForm({
            "event_year": "",
            "event_era": "",
            "event_description": "",
            
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors["event_year"],
            ['This field is required.']
        )
        self.assertEqual(
            form.errors["event_era"],
            ['This field is required.']
        )
        self.assertEqual(
            form.errors["event_description"],
            ['This field is required.']
        )
    
    def test_cannot_validate_form_with_non_numeric_event_year_with_messages(self):
        form = HistoryEventForm({
            "event_year": "asdf",
            "event_era": "AC",
            "event_description": "This is a test",
            
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors["event_year"],
            ['Enter a whole number.']
        )