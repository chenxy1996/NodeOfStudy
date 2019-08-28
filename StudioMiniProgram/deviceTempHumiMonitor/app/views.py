from django.views import View
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

import sys
sys.path.append("..")

from my_util.test_util import *
from configure import *


'''
Mimicking_Info_Sender： 模拟从数据库中得到 http request 需要的数据并发送 json 数据对象
'''
class Mimicking_Info_Sender(View):
    def get(self, request, num):
        return_json_data = {}

        if num <= MAX_DATA_REQUEST_NUMBER:
            return_json_data["data"] = get_arbitary_data_list(num)
            return_json_data["dataNum"] = num
        else:
            return_json_data["data"] = []
            return_json_data["dataTotalNumber"] = 0

        return JsonResponse(return_json_data, safe=False)
        
