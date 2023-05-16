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
# from django.utils import timezone
from django.utils.timezone import make_aware
from ..models.watched_match import WatchedMatchCard
from ..models.match import Match
from ..serializers import WatchedMatchSerializer, WatchedMatchReadSerializer
from ..serializers import MatchSerializer, MatchIdSerializer

@api_view(['GET',])
@renderer_classes([JSONRenderer])
def create_and_get_cards(request, date):


    formated_date = datetime.strptime(date, "%Y%m%d")
    # formated_date = make_aware(datetime.strptime(date, "%Y%m%d"))
    # print("aware datetime")
    # print(formated_date)

    day_min = make_aware(datetime.combine(formated_date, datetime.today().time().min))
    # formated_min = day_min.strftime("%Y-%m-%dT%H:%M:%S")
    
    day_max = make_aware(datetime.combine(formated_date, datetime.today().time().max))
    # formated_max = day_max.strftime("%Y-%m-%dT%H:%M:%S")

    # print("max")
    # print(day_max)
    # print(formated_max)

    # get matches for this date
    # matches = Match.objects.filter(date_time__range=(formated_min, formated_max))
    matches = Match.objects.filter(date_time__range=(day_min, day_max))
    

    # for each match
    for match in matches:
        try:
            found_card = WatchedMatchCard.objects.get(match=match.match_id)
        except WatchedMatchCard.DoesNotExist:
            found_card = None

        #if the match is not in the db, create it
        if found_card == None:
            # add the user to the request data
            if not "user" in request.data:
                request.data["user"] = request.user.id

            request.data["match"] = match.match_id
            
            serializer = WatchedMatchSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
            else: print(serializer.errors)


    # get watch cards for this date
    watched_matches = WatchedMatchCard.objects.filter(user = request.user.id).filter(match__date_time__range=(day_min, day_max))

    # return all watch cards for this date
    serializer = WatchedMatchReadSerializer(watched_matches, many=True)
    return Response(serializer.data)





