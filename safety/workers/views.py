from django.views import View
from django.http import HttpResponse
from .models import Worker
from django.shortcuts import render
import json
# class-base view

class WorkerListView(View):
    def get(self, request):
        workers = Worker.objects.all()
       # print(workers)
       
       
       # html = ''
       # for worker in workers:
        #    html += f'<li>{worker.first_name}</li>'

        worker_list = []
        for worker in workers:
            d = {
                'name': worker.first_name
            }
            worker_list.append(d)

        return HttpResponse (
            json.dumps(worker_list),
            content_type='application/json'
        )
        #return render(request, 'worker_list.html', {
        #    'workers': workers
        #})
