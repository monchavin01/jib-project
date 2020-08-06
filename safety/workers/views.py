from django.views import View
from django.http import HttpResponse

# class-base view
class WorkerListView(View):
    def get(self, request):
        return HttpResponse()
