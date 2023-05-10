from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.middleware.csrf import get_token

from datetime import datetime, timezone
from ..models.match import Match
from ..serializers import MatchSerializer, MatchIdSerializer

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
        # print(date)
        formated_date = datetime.strptime(date, "%Y%m%d")

        day_min = datetime.combine(formated_date, datetime.today().time().min)
        formated_min = day_min.strftime("%Y-%m-%dT%H:%M:%S")
        # need to make this timezone aware...
        min_with_timezone = day_min.replace(tzinfo=timezone.utc)

        day_max = datetime.combine(formated_date, datetime.today().time().max)
        max_with_timezone = day_max.replace(tzinfo=timezone.utc)

        formated_max = day_max.strftime("%Y-%m-%dT%H:%M:%S")
        # formated_max = formated_max.replace(tzinfo=timezone.utc)
        print("******************")
        print(formated_date)
        # print(day_max)
        # print(max_with_timezone)
        # print(formated_max)
        print("******************")


        # matches = Match.objects.all()
        # matches = Match.objects.filter(date_time__range=(formated_min, formated_max))
        matches = Match.objects.filter(date_time__range=(min_with_timezone, max_with_timezone))
        serializer = MatchIdSerializer(matches, many=True)
        return Response(serializer.data)