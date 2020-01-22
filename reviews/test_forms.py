from django.test import TestCase
from reviews.forms import ReviewForm

class TestHistoryEventForm(TestCase):
    """
    Tests for valid Review forms
    """
    def test_cannot_create_form_with_missing_fields_with_messages(self):
        form = ReviewForm({
            "review_owner_name": "",
            "review_detail": "",
            
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors["review_owner_name"],
            ['This field is required.']
        )
        self.assertEqual(
            form.errors["review_detail"],
            ['This field is required.']
        )
    