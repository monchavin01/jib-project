

from django.urls import path
from .views import Covid19ReportView


urlpatterns = [
   
 
    path('', Covid19ReportView.as_view())
]
