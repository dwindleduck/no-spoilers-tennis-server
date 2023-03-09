from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status, generics
from rest_framework.response import Response 

from .models.match import Match
from .serializers import MatchSerializer

import http.client
import requests



def update_stored(req_data):
    print("Updating Stored Match Data")
    # for each league in the req_data
    for tournament in req_data["Stages"]:
        # for each match in the league
        for match in tournament["Events"]:
            #assemble request object
            match_to_process = {
                # map to LiveScore field names
                'match_id': match["Eid"],
                'date_time': match["Esd"] ,
                'league': tournament["Cnm"],
                'competition': tournament["Snm"],
                #update names for doubles
                #defaulting to grab the first player only
                'T1name': match["T1"][0]["Nm"],
                'T2name': match["T2"][0]["Nm"],
            }
            if "Tr1" in match:
                match_to_process['T1SetScore']: match["Tr1"]

            if "Tr2" in match:  
                match_to_process['T2SetScore']: match["Tr2"]

            #add tiebreak scores

            if "Tr1S1" in match:  
                match_to_process['T1Set1']: match["Tr1S1"]
            else: match_to_process['T1Set1']: "0"
            if "Tr2S1" in match:  
                match_to_process['T2Set1']: match["Tr2S1"]
            else: match_to_process['T2Set1']: "0"
            if "Tr1S2" in match:  
                match_to_process['T1Set2']: match["Tr1S2"]
            else: match_to_process['T1Set2']: "0"  
            if "Tr2S2" in match:  
                match_to_process['T2Set2']: match["Tr2S2"]
            else: match_to_process['T2Set2']: "0"
            if "Tr1S3" in match:  
                match_to_process['T1Set3']: match["Tr1S3"]
            else: match_to_process['T1Set3']: "0"
            if "Tr2S3" in match:  
                match_to_process['T2Set3']: match["Tr2S3"]
            else: match_to_process['T2Set3']: "0"
            if "Tr1S4" in match:  
                match_to_process['T1Set4']: match["Tr1S4"]
            else: match_to_process['T1Set4']: "0"
            if "Tr2S4" in match:  
                match_to_process['T2Set4']: match["Tr2S4"]
            else: match_to_process['T2Set4']: "0"
            if "Tr1S5" in match:  
                match_to_process['T1Set5']: match["Tr1S5"]
            else: match_to_process['T1Set5']: "0"
            if "Tr2S5" in match:  
                match_to_process['T1Set5']: match["Tr2S5"]
            else: match_to_process['T1Set5']: "0"


            if "Eps" in match:  
                match_to_process['status']: match["Eps"]
            else: match_to_process['status']: "0"
            if "Ewt" in match:  
                match_to_process['winner']: match["Ewt"]
            else: match_to_process['winner']: "0"
            
            # print(match_to_process)
            
            try:
                match = Match.objects.get(pk=match_to_process["match_id"])
            except Match.DoesNotExist:
                match = None
            
            # print(match)

            #if the match is in the db
            if match == None:
                print("match == None")
                #post new match

                #match_to_process is not a valid QueryDict
                serializer = MatchSerializer(data=match_to_process)
                if serializer.is_valid():
                    serializer.save()
                    print("Saved new match")
            else:
                print("else")
                #patch existing match
                serializer = MatchSerializer(match, data=match_to_process)
                if serializer.is_valid():
                    serializer.save()
                    print("Saved updated match")
            
                






def list_by_date(request):
    url = "https://livescore6.p.rapidapi.com/matches/v2/list-by-date"
   
    querystring = {"Category":"tennis","Date":"20230309","Timezone":"-7"}

    headers = {
        "X-RapidAPI-Key": "9b71ef6a10msh3f6d5e6bda5aa3ap1a62c2jsnf9ceb39aa5f4",
        "X-RapidAPI-Host": "livescore6.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    # use response data to update the stored match data
    update_stored(response.json())
   
    # print(response.text)
    
    return JsonResponse(response.json(), safe=False)






def competition_detail(request):
    # print(request)
    # url = "https://livescore6.p.rapidapi.com/competitions/detail"

    # need to get CompId from request
    # querystring = {"CompId":{get CompId from request},"Timezone":"-7"}

    # headers = {
    #     "X-RapidAPI-Key": "9b71ef6a10msh3f6d5e6bda5aa3ap1a62c2jsnf9ceb39aa5f4",
    #     "X-RapidAPI-Host": "livescore6.p.rapidapi.com"
    # }

    # response = requests.request("GET", url, headers=headers, params=querystring)
    # print(response.text)
    
    # return JsonResponse(response.json(), safe=False)
    print("Competition Detail Function Call")
    return HttpResponse("Competition Detail Function Call")



