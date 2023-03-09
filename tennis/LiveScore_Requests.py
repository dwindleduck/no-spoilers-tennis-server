from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status, generics
from rest_framework.response import Response 

import http.client
import requests

def list_by_date(request):
    # print(request)
    # url = "https://livescore6.p.rapidapi.com/matches/v2/list-by-date"

    # querystring = {"Category":"tennis","Date":"20230308","Timezone":"-7"}

    # headers = {
    #     "X-RapidAPI-Key": "9b71ef6a10msh3f6d5e6bda5aa3ap1a62c2jsnf9ceb39aa5f4",
    #     "X-RapidAPI-Host": "livescore6.p.rapidapi.com"
    # }

    # response = requests.request("GET", url, headers=headers, params=querystring)
    # print(response.text)
    
    # return JsonResponse(response.json(), safe=False)
    return HttpResponse("List By Date Function Call")






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
    return HttpResponse("Competition Detail Function Call")



