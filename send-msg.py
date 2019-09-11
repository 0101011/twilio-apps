from twilio.rest import Client

# Type your cell phone number with WhatsApp installed:
your_num = '+123456789'

# Cell phone number of the reciver of your messages:
to = '+987654321'

# Reading client credentials from TWILIO_ACCOUNT_SID and AUTH_TOKEN:
client = Client()

# Defining sender and receiver of messages:
from_num = f'whatsapp:{your_num}'
to_num = f'whatsapp:{to}'

client.messages.create(body='Hello, world!',
                       from_=from_num,
                       to=to_num)
