from django.shortcuts import render
import time
from .thread import CreateStudentsThread
from asgiref.sync import sync_to_async, async_to_sync
from channels.layers import get_channel_layer
import json
# Create your views here.
def homeview(request):
    # print(request.user)
    # for i in range(0,10):
    #     channel_layer=get_channel_layer()
    #     data={'count':i}
    #     async_to_sync(channel_layer.group_send)(
    #         'new_group_room',{
    #             'type':'send_notification',
    #             'value':json.dumps(data)
    #         }
    #     )
    #     time.sleep(1)
    return render(request, 'index.html')

from django.http import JsonResponse

def generate_student_data(request):
    total = request.GET.get('total')
    CreateStudentsThread(int(total)).start()
    return JsonResponse({'status' : 200})