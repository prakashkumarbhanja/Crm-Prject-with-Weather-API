from cgitb import reset
from http import server
import json
from re import S
import re
from tkinter.messagebox import NO
from urllib import response
from rest_framework.serializers import Serializer
# import stripe

from datetime import datetime

from django.conf import settings
from django.contrib.auth.models import User
from django.http import Http404, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
# from stripe import webhook
# from stripe.api_resources import line_item

from team.models import Team
from team.serializers import TeamSerializer, UserSerializer


class TeamViewSet(viewsets.ModelViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()

    def get_queryset(self):
        return self.queryset.filter(members__in=[self.request.user]).first()

    def perform_create(self, serializer):
        obj = serializer.save(created_by=self.request.user)
        obj.members.add(self.request.user)
        obj.save()

class UserDetail(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(data = user)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET'])
def get_my_team(request):
    team = Team.objects.filter(members__in = [request.user]).first()
    serilizer = TeamSerializer(team)
    return Response(serilizer.data) 


@api_view(['GET'])
def add_member(request):
    team = Team.objects.filter(members__in=[request.user]).first()
    email = request.data['email']

    print('Email', email)

    user = User.objects.get(username=email)

    team.members.add(user)
    team.save()

