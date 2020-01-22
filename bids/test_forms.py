from django.test import TestCase
from bids.forms import BidDetailsForm

class TestBidDetailsForm(TestCase):
    """
    Tests for valid Bid Details forms
    """
    
    def test_cannot_create_form_with_missing_bid_amount_with_messages(self):
        form = BidDetailsForm({
            "bid_amount": "",
            "bid_quantity": 12.01
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors["bid_amount"],
            ['This field is required.']
        )
    
    def test_cannot_create_form_with_missing_bid_quantity_with_messages(self):
        form = BidDetailsForm({
            "bid_amount": 1,
            "bid_quantity": ""
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors["bid_quantity"],
            ['This field is required.']
        )
    
    def test_cannot_create_form_with_non_numeric_input_with_messages(self):
        form = BidDetailsForm({
            "bid_amount": "asdf",
            "bid_quantity": "fdsa"
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors["bid_amount"],
            ['Enter a number.']
        )
        self.assertEqual(
            form.errors["bid_quantity"],
            ['Enter a whole number.']
        )