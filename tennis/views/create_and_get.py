from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.middleware.csrf import get_token
from django.http import JsonResponse

from datetime import datetime
from ..models.watched_match import WatchedMatchCard
from ..serializers import WatchedMatchSerializer, WatchedMatchReadSerializer


@api_view(['GET',])
@renderer_classes([JSONRenderer])
def create_and_get_cards(request, date):
    print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    # get watch cards for this date
    formated_date = datetime.strptime(date, "%Y%m%d")

    day_min = datetime.combine(formated_date, datetime.today().time().min)
    formated_min = day_min.strftime("%Y-%m-%dT%H:%M:%S")
    day_max = datetime.combine(formated_date, datetime.today().time().max)
    formated_max = day_max.strftime("%Y-%m-%dT%H:%M:%S")

    watched_matches = WatchedMatchCard.objects.filter(user = request.user.id).filter(match__date_time__range=(formated_min, formated_max))
    # watched_matches = WatchedMatchCard.objects.all().filter(user = request.user.id)
    serializer = WatchedMatchReadSerializer(watched_matches, many=True)
    return Response(serializer.data)

    # get match_ids for this date

    # if a watch card does not exist for a given match_id, create it
    # return all watch cards for this date


