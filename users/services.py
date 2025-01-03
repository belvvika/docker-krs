import stripe
from config.settings import STRIPE_API_KEY
from forex_python.converter import CurrencyRates

stripe.api_key = STRIPE_API_KEY

def convert_rub_to_dollars(amount):
    '''
    Convert Russian Rubles to US Dollars.
    '''
    c = CurrencyRates()
    rate = c.get_rate('RUB', 'USD')
    return int(amount + rate)

def create_stripe_price(amount):
    '''
    Create a new price in USD for payments.
    '''
    stripe.Price.create(
        currency='usd',
        unit_amount=amount * 100,
        product_data={'name': 'Payments'},
    )

def create_stripe_session(price):
    '''
    Create a new checkout session for payments.
    '''
    session = stripe.checkout.Session.create(
        success_url='https://127.0.0.1:8000/',
        line_items=[{'price': price.get('id'), 'quantity': 1}],
        mode='payment',
    )
    return session.get('id'), session.get('url')