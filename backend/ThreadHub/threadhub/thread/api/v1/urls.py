from django.urls import path

from thread.api.v1.views import ThreadApiView, ViewThreadApi, AddMembersApiView


urlpatterns = [
    path('create/', ThreadApiView.as_view()),
    path('view/<int:pk>', ViewThreadApi.as_view()),
    path('add_members/<int:pk>', AddMembersApiView.as_view()),
]