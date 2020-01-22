from django.test import TestCase
from payment.forms import OrderDetailsForm

class TestOrderDetailsForm(TestCase):
    """
    Tests for valid Order Details form
    """
    def test_cannot_create_form_with_missing_fields_with_messages(self):
        form = OrderDetailsForm({
            "full_name": "",
            "phone_number": "",
            "address_line1": "",
            "address_line2": "",
            "town_or_city": "",
            "county_or_province_or_state": "",
            "country": "",
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors["full_name"],
            ['This field is required.']
        )
        self.assertEqual(
            form.errors["phone_number"],
            ['This field is required.']
        )
        self.assertEqual(
            form.errors["address_line1"],
            ['This field is required.']
        )
        self.assertEqual(
            form.errors["address_line2"],
            ['This field is required.']
        )
        self.assertEqual(
            form.errors["town_or_city"],
            ['This field is required.']
        )
        self.assertEqual(
            form.errors["county_or_province_or_state"],
            ['This field is required.']
        )
        self.assertEqual(
            form.errors["county_or_province_or_state"],
            ['This field is required.']
        )
    
    def test_can_create_form_with_missing_postcode_with_messages(self):
        form = OrderDetailsForm({
            "full_name": "TEST",
            "phone_number": "TESt",
            "address_line1": "TEST",
            "address_line2": "TEST",
            "town_or_city": "TEST",
            "postcode": "",
            "county_or_province_or_state": "TEST",
            "country": "TEST",
        })
        print(form.errors)
        self.assertTrue(form.is_valid())