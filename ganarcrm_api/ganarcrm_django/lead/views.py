from traceback import print_tb
from urllib import request
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets

from lead.models import (Lead)
from team.models import (Team)
from lead.serializer import *


class LeadViewSet(viewsets.ModelViewSet):
    serializer_class = LeadSerializer
    queryset = Lead.objects.all()

    def get_queryset(self):
        team = Team.objects.filter(members__in=[self.request.user]).first()
        return self.queryset.filter(team=team)

    def perform_create(self, serializer):
        print('-this is only data-', self.request.data)
        """
        if Using only data than,
        
        data = self.request.data
        data['created_by'] = self.request.user
        Lead.objects.create(**data)
        """
        print("-----This is serializer and seializer have save()-------",serializer)
        team = Team.objects.filter(members__in=[self.request.user]).first()
        
        serializer.save(team=team, created_by=self.request.user)

    def perform_update(self, serializer):

        print("--Object--",self.get_object())
        print("--Updated serializer--", serializer)

        obj = self.get_object()

        member_id = self.request.data['assigned_to']

        if member_id:
            user = User.objects.get(pk=member_id)
            serializer.save(assigned_to = user)
        else:
            serializer.save()

       



