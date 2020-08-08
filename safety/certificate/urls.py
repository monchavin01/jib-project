from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import (
    CertificateModelViewSetView
    #WorkerModelViewSetView,
)

router = DefaultRouter()
router.register(r'', CertificateModelViewSetView)





urlpatterns = [
   # path('',WorkerListView.as_view()),
    path('',include(router.urls)),

]
