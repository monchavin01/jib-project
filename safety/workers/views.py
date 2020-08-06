from django.views import View
from django.http import HttpResponse
from .models import Worker
from django.shortcuts import render
# class-base view

class WorkerListView(View):
    def get(self, request):
        workers = Worker.objects.all()
        print(workers)
        html = ''
        for worker in workers:
            html += f'<li>{worker.first_name}</li>'
        return render(request, 'worker_list.html', {})
