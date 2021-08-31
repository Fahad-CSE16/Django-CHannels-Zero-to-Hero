import channels
from django.db import models
from django.contrib.auth.models import User

from asgiref.sync import sync_to_async, async_to_sync
from channels.layers import get_channel_layer
import json

class Notifications(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    text=models.CharField(max_length=100)
    is_seen=models.BooleanField(default=False)
    def save(self, *args, **kwargs):
        super(Notifications, self).save(*args, **kwargs)
        channel_layer=get_channel_layer()
        count=Notifications.objects.filter(is_seen=False).count()
        data={'count':count,'notification':self.text}
        async_to_sync(channel_layer.group_send)(
            'test_group_room',{
                'type':'send_notification',
                'value':json.dumps(data)
            }
        )
class Students(models.Model):
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    age = models.IntegerField()
    
    def __str__(self):
        return self.student_name