import stripe


class StripeApi:

    def get_session(amount):
        stripe.api_key = 'sk_test_KBYsre7HUl3HZ9GFhJulO9Sw00tZy63dmI'

        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'name': 'Donation',
                'description': 'Donation for Bibleit',
                'images': ['https://example.com/t-shirt.png'],
                'amount': amount,
                'currency': 'usd',
                'quantity': 1,
            }],
            success_url='https://example.com/success?session_id={CHECKOUT_SESSION_ID}',
            cancel_url='https://example.com/cancel',
        )

        return session
