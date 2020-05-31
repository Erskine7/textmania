# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import os
from dotenv import load_dotenv
from twilio.http.http_client import TwilioHttpClient


texter = os.path.expanduser('~/texter')  # adjust as appropriate
load_dotenv(os.path.join(texter, 'twilio_account_sid.env'))
load_dotenv(os.path.join(texter, 'twilio_auth_token.env'))
proxy_client = TwilioHttpClient(proxy={'http': os.environ['http_proxy'],
                                       'https': os.environ['https_proxy']})


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'twilio_account_sid.env'
auth_token = 'twilio_account_token.env'
client = Client(account_sid, auth_token, http_client=proxy_client)

message = client.messages \
    .create(
         body='Erskine has safely deployed this texting code.',
         from_='+12073832573',
         to='+15163430763'
     )

print(message.sid)