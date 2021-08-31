from .models import RoomName
from django.contrib.auth.models import User
from .serializers import *
import json

def validate_then_get_room(room_name):
    try:
        room = RoomName.objects.get(room_name=room_name)
        
    except RoomName.DoesNotExist:
        return None
    except User.DoesNotExist:
        return None
    return room


def support_room_exist(room_username, user_username):
    try:
        room = RoomName.objects.get(room_name=room_username)
        user = User.objects.get(username=user_username)
    except RoomName.DoesNotExist:
        return False
    except User.DoesNotExist:
        return False
    if room:
        return True


def user_has_room_access(user,room):
    if user not in room.participants.all():
        return False
    else:
        return True

def get_previous_msg(room):
    queryset=room.room.all().order_by('-created_at')[:40]
    queryset2=sorted(queryset, key=lambda x: x.created_at)
    messages = MessageSerializer(queryset2, many=True)
    return json.dumps(messages.data)