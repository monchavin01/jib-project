from django.urls import include, path
from .views import WorkerListView



urlpatterns = [
    path('',WorkerListView.as_view())
]
