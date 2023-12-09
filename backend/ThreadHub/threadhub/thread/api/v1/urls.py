from django.urls import path

from thread.api.v1.views import ThreadApiView


urlpatterns = [
    path('create/', ThreadApiView.as_view()),
]