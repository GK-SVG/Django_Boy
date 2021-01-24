import os
from twilio.rest import Client


account_sid = 'Your Account SID'
        auth_token = 'Your Auth Token'

def send_code(phone_number,code):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
                            body=f"Your Login Verification code is {code}",
                            from_='Twilio Phone Number',
                            to   ='Phone Number on which sms send'
                            )
    print(message.sid)