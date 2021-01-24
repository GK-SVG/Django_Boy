from django.db import models
import os
from twilio.rest import Client
# Create your models here.
class SMS(models.Model):
    mysms = models.CharField(max_length=200)
    def save(self, *args, **kwargs):
        account_sid = 'Your Account SID'
        auth_token = 'Your Auth Token'
        client = Client(account_sid, auth_token)
        message = client.messages.create(
                            body={self.mysms},
                            from_='Twilio Phone Number',
                            to   ='Phone Number on which sms send'
                            )
        print(message.sid)
        return super().save(*args, **kwargs)