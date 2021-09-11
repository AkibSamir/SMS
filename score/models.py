from django.db import models
import os
from twilio.rest import Client

# Create your models here.
class Score(models.Model):
    result = models.PositiveIntegerField()

    def __str__(self):
        return str(self.result)

    def save(self, *args, **kwargs):
        account_sid = 'ACa034a16430a3e5c1e544a075a197809e'
        auth_token = '4c1c4f42d28e4826d54abe1ead061fab'
        client = Client(account_sid, auth_token)

        message = client.messages \
                        .create(
                            body=f"To go to sleep at night, I imagine you are here, next to me, with your (hair color) hair in a messy bun, just cuddled next to me; just how I want us to be. {self.result}",
                            from_='+15033601572',
                            to='+8801728619816'
                        )

        print(message.sid)
        return super().save(*args, **kwargs)
