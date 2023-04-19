from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.middleware.csrf import get_token

from datetime import datetime
from ..models.match import Match
from ..serializers import MatchSerializer

# Create your views here.
class Matches(generics.ListCreateAPIView):
    """
    A view for creating and viewing all matches

    /matches/<str:date>
    """
    queryset = ()
    serializer_class = MatchSerializer

    # def get(self, request):
    #     """Index all"""
    #     matches = Match.objects.all()
    #     # .filter(owner = request.user)
    #     serializer = MatchSerializer(matches, many=True)
    #     return Response(serializer.data)
    

    def get(self, request, date):
        """Index by date"""
        print(date)
        formated_date = datetime.strptime(date, "%Y%m%d")

        day_min = datetime.combine(formated_date, datetime.today().time().min)
        formated_min = day_min.strftime("%Y-%m-%dT%H:%M:%S")
        day_max = datetime.combine(formated_date, datetime.today().time().max)
        formated_max = day_max.strftime("%Y-%m-%dT%H:%M:%S")

        # matches = Match.objects.all()
        matches = Match.objects.filter(date_time__range=(formated_min, formated_max))
        serializer = MatchSerializer(matches, many=True)
        return Response(serializer.data)