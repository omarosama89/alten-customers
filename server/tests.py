from unittest import TestCase
from django.test import TransactionTestCase
from .models import Customer

class CustomerModelTestCase(TestCase):

    def test_valid_model_first_name_exists(self):
        target = Customer()
        target.first_name = 'Ahmed'
        self.assertTrue(target.first_name)

    def test_invalid_model_first_name_not_exists(self):
        target = Customer()
        self.assertFalse(target.first_name)

    def test_valid_model_last_name_exists(self):
        target = Customer()
        target.last_name = 'dafrawy'
        self.assertTrue(target.last_name)

    def test_invalid_model_last_name_not_exists(self):
        target = Customer()
        self.assertFalse(target.last_name)

    def test_valid_model_address_exists(self):
        target = Customer()
        target.address = '11 fawzy st.,'
        self.assertTrue(target.address)

    def test_invalid_model_address_not_exists(self):
        target = Customer()
        self.assertFalse(target.address)


class DatabaseLoaded(TransactionTestCase):
    fixtures = ['server/fixtures/unit-test.json']

    def test_fixtures_load(self):
        self.assertTrue(Customer.objects.count() > 0)

# class CustomerModelTransactionTestCase(TransactionTestCase):
#     # fixtures = ['server/fixtures/unit-test.json']
#
#     def test_first_name_persists(self):
#         new_first_name = 'kjhkjdfhkjahskj'
#         target = Customer.objects.first()
#         target.first_name = new_first_name
#         target.save()
#         self.assertEqual(target.first_name, Customer.objects.get(pk=target.pk).first_name)
