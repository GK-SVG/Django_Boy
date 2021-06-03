from django.db import models
from django.contrib.auth.models import User
import json
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
# Create your models here.


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    is_seen = models.BooleanField(default=False)


    def save(self,*args, **kwargs):
        channel_layer = get_channel_layer()
        count = Notification.objects.filter(is_seen=False).count()
        data = {"count":count,"notification":self.text}
        async_to_sync(channel_layer.group_send)(
            "test_room_group",{
                'type' : 'send_notification',
                'value' : json.dumps(data)
            }
        )
        super(Notification, self).save(*args, **kwargs)
