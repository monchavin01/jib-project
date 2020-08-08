from django.views import View
from django.http import HttpResponse

import requests

class Covid19ReportView(View):
    def get(self, request):
        requests.get('https://covid19.th-stat.com/api/open/today')
        return HttpResponse()


# Create your views here.

