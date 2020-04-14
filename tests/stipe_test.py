import unittest
from stripe_calls.stripe_api import StripeApi


class TestStripeAPI(unittest.TestCase):

    def test_construct_session(self):
        session = StripeApi.get_session(amount=500)
        print(session)
        self.assertTrue(session is not None)
