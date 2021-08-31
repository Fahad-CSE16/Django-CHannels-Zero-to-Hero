from django.db import models
from django.contrib.auth.models import User
from asgiref.sync import  async_to_sync
from channels.layers import get_channel_layer
import json

class RoomName(models.Model):
    room_name = models.CharField(max_length=40, unique=True)
    admin = models.ForeignKey( User, related_name='users_group', on_delete=models.CASCADE)
    participants = models.ManyToManyField( User, related_name='group_chats', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.room_name


class Message(models.Model):
    msg=models.TextField()
    group=models.ForeignKey(RoomName, on_delete=models.CASCADE,related_name='room')
    from_user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='frm')
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=['-created_at']
    def __str__(self):
        return self.msg
    def save(self, *args, **kwargs):
        super(Message, self).save(*args, **kwargs)
        # channel_layer=get_channel_layer()
        # count=Message.objects.filter().count()
        # data={'id':self.id,'msg':self.msg,'to_user':self.to_user.username,'from_user':self.from_user.username}
        # async_to_sync(channel_layer.group_send)(
        #     'chat_group',{
        #         'type':'send_notification',
        #         'value':json.dumps(data)
        #     }
        # )