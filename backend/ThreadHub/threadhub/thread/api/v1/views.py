from django.shortcuts import render
from django.db.utils import IntegrityError
from rest_framework import status
from rest_framework import serializers
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, inline_serializer

from thread.models import Thread
from thread.api.v1.serializers import ThreadSerializer
from authentication.models import CustomUser



class ThreadApiView(CreateAPIView):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer
    permission_classes = [IsAuthenticated]


    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                thread = Thread.objects.get(pk=serializer.data['pk'])
                thread.members.add(request.user.pk)
                return Response(
                    {"status": "created", "name": serializer.data["name"]},
                    status=status.HTTP_201_CREATED,
                )
            except IntegrityError as e:
                return Response(
                    {"status": "error - name is invalid"},
                    status=status.HTTP_409_CONFLICT,
                )
        return Response(
            {"status": "error - Invalid data"},
            status=status.HTTP_422_UNPROCESSABLE_ENTITY,
        )
    
