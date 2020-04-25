import stripe
from flask_api import status


class StripeApi:
    stripe.api_key = 'sk_test_KBYsre7HUl3HZ9GFhJulO9Sw00tZy63dmI'
    endpoint_secret = 'whsec_...'

    def get_session(amount):
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'name': 'Donation',
                'description': 'Donation for Bibleit',
                'images': ['https://picsum.photos/280/320?random=4'],
                'amount': amount,
                'currency': 'usd',
                'quantity': 1,
            }],
            success_url='http://localhost:8000/donate/success?session_id={CHECKOUT_SESSION_ID}',
            cancel_url='http://localhost:8000/cancel',
        )
        return session

    @classmethod
    def call_webhooks(cls, request):
        payload = request.body
        sig_header = request.META['HTTP_STRIPE_SIGNATURE']
        event = None

        try:
            event = stripe.Webhook.construct_event(
                payload, sig_header, endpoint_secret
            )
        except ValueError as e:
            # Invalid payload
            # return HttpResponse(status=400)
            return status.HTTP_400_BAD_REQUEST
        except stripe.error.SignatureVerificationError as e:
            # Invalid signature
            return status.HTTP_400_BAD_REQUEST

        # Handle the checkout.session.completed event
        if event['type'] == 'checkout.session.completed':
            session = event['data']['object']

            # Fulfill the purchase...
            StripeApi.handle_checkout_session(session)

        return status.HTTP_200_OK

    @classmethod
    def handle_checkout_session(cls, session):
        # send email
        pass
