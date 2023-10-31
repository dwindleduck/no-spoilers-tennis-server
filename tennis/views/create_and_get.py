from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from ..LiveScore_Requests import list_by_date

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.middleware.csrf import get_token
from django.http import JsonResponse

from datetime import datetime, timedelta
from django.utils import timezone
from django.utils.timezone import make_aware
from ..models.watched_match import WatchedMatchCard
from ..models.match import Match
from ..serializers import WatchedMatchSerializer, WatchedMatchReadSerializer
from ..serializers import MatchSerializer, MatchIdSerializer

@api_view(['GET',])
@renderer_classes([JSONRenderer])
def create_and_get_cards(request, date):
    selectedDate = date
    now = timezone.now()
    inRange = False
    matchesLastUpdated = None
    needsUpdating = False

    # Restrict the time to just the requested day (00:00:00-23:59:59)
    formated_date = datetime.strptime(selectedDate, "%Y%m%d")
    day_min = make_aware(datetime.combine(formated_date, datetime.today().time().min))
    day_max = make_aware(datetime.combine(formated_date, datetime.today().time().max))

    # this returns an array of match_ids
    matches = Match.objects.filter(date_time__range=(day_min, day_max))
    
    # check one match for if it was last updated more than three hours ago
    if matches :
        matchesLastUpdated = matches[0].updated_at
        tdelta = now - matchesLastUpdated
        if tdelta.seconds > 10800 : # 10800 seconds is three hours
            needsUpdating = True


    # check if the selected date is in range
    # (1 previous day or next 3 days)
    date_range = [now - timedelta(days=x) for x in range(-3, 2)]
    for date in date_range:
        dateToCheck = date.strftime("%Y%m%d")
        if dateToCheck == selectedDate:
            inRange = True
            # Still need to Handle for no matches today (nothing will ever return)
            if matchesLastUpdated == None :
                needsUpdating = True


    # if the selected day is with within range
    # and it updated more than three hours ago
    if inRange and needsUpdating:
        # refresh LiveScore_Request
        list_by_date(formated_date)
        # and .filter() matches again
        matches = Match.objects.filter(date_time__range=(day_min, day_max))
    





    # for each match
    for match in matches:
        try:
            found_card = WatchedMatchCard.objects.get(match=match.match_id, user = request.user.id)
        except WatchedMatchCard.DoesNotExist:
            found_card = None
        except WatchedMatchCard.MultipleObjectsReturned:
            #should never happen - model only accepts unique pairs
            pass


        # print(found_card)
        #if the match is not in the db, create it
        if found_card == None:
            # add the user to the request data
            # the Watched_Matches model requires a unique pair of 'user' and 'match'
            if not "user" in request.data:
                request.data["user"] = request.user.id

            request.data["match"] = match.match_id
            
            # create and save
            print("Create " + match.match_id)
            serializer = WatchedMatchSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
            else: print(serializer.errors)


    # get watch cards for this date
    watched_matches = WatchedMatchCard.objects.filter(user = request.user.id).filter(match__date_time__range=(day_min, day_max))

    # return all watch cards for this date
    serializer = WatchedMatchReadSerializer(watched_matches, many=True)
    return Response(serializer.data)





