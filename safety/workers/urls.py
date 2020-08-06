from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import (
    WorkerListView,
    WorkerModelViewSetView,
)

router = DefaultRouter()
router.register(r'', WorkerModelViewSetView)





urlpatterns = [
    path('xxx',WorkerListView.as_view()),
    path('',include(router.urls)),

]
