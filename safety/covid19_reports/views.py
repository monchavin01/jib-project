from django.views import View
from django.http import HttpResponse

class Covid19ReportView(View):
    def get(self, request):
        return HttpResponse()


# Create your views here.

