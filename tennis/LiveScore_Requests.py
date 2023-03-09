from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status, generics
from rest_framework.response import Response 

from .views.match_views import Matches, MatchDetail

import http.client
import requests




def list_by_date(request):
    print(request)
    print("List By Date Function Call")


    url = "https://livescore6.p.rapidapi.com/matches/v2/list-by-date"
   
    querystring = {"Category":"tennis","Date":"20230309","Timezone":"-7"}

    headers = {
        "X-RapidAPI-Key": "9b71ef6a10msh3f6d5e6bda5aa3ap1a62c2jsnf9ceb39aa5f4",
        "X-RapidAPI-Host": "livescore6.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)


    #### use response data to update the stored match data

    # for each league in the response
    # for league in response.text["Stages"]:
        # for each match in the league
        # for match in stage["Events"]:
            #assemble response object
            # match_to_process = {
                # update these to LiveScore field names
                # 'date_time': match["Esd"] ,
                # 'league': league["Cnm"],
                # 'competition': league["Snm"],
                ### update team names for doubles
                # 'T1name': match["T1"][0]["Nm"],
                # 'T2name': match["T2"][0]["Nm"],
                # 'T1SetScore': match["Tr1"],
                # 'T2SetScore': match["Tr2"],
                # 'T1Set1': match["Tr1S1"],
                # 'T2Set1': match["Tr2S1"],
                # 'T1Set2': match["Tr1S2"],
                # 'T2Set2': match["Tr2S2"],
                # 'T1Set3': match["Tr1S3"],
                # 'T2Set3': match["Tr2S3"],
                # 'T1Set4': match["Tr1S4"],
                # 'T2Set4': match["Tr2S4"],
                # 'T1Set5': match["Tr1S5"],
                # 'T2Set5': match["Tr2S5"],
                # 'winner': match["Ewt"],
            # }
            #if the match is in the db
                #MatchDetail.patch(self, match_to_process)
            #else
                #Matches.post(self, match_to_process)

    print(response.text)
    
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



