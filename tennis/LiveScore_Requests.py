from django.http import JsonResponse
import requests
from datetime import datetime
from .models.match import Match
from .serializers import MatchSerializer

def update_stored(req_data):
    # for each league in the req_data
    for tournament in req_data["Stages"]:
        # for each match in the league
        for match in tournament["Events"]:
            #format datetime
            recieved_datetime = str(match["Esd"])
            date_object = datetime.strptime(recieved_datetime, "%Y%m%d%H%M%S")
            formated_date = date_object.strftime("%Y-%m-%dT%H:%M:%S")

            #assemble request object
            match_to_process = {
                # map to LiveScore field names
                'match_id': match["Eid"],
                'date_time': formated_date,
                'league': tournament["Cnm"],
                'competition': tournament["Snm"],
                #update names for doubles
                #defaulting to grab the first player only
                'T1name': match["T1"][0]["Nm"],
                'T2name': match["T2"][0]["Nm"],
            }

            if "Tr1" in match:
                match_to_process['T1SetScore'] = match["Tr1"]

            if "Tr2" in match:  
                match_to_process['T2SetScore'] = match["Tr2"]

            #add tiebreak scores
            if "Tr1S1" in match:  
                match_to_process['T1Set1'] = match["Tr1S1"]
            else: match_to_process['T1Set1'] = "0"
            if "Tr2S1" in match:  
                match_to_process['T2Set1'] = match["Tr2S1"]
            else: match_to_process['T2Set1'] = "0"
            if "Tr1S2" in match:  
                match_to_process['T1Set2'] = match["Tr1S2"]
            else: match_to_process['T1Set2'] = "0"  
            if "Tr2S2" in match:  
                match_to_process['T2Set2'] = match["Tr2S2"]
            else: match_to_process['T2Set2'] = "0"
            if "Tr1S3" in match:  
                match_to_process['T1Set3'] = match["Tr1S3"]
            else: match_to_process['T1Set3'] = "0"
            if "Tr2S3" in match:  
                match_to_process['T2Set3'] = match["Tr2S3"]
            else: match_to_process['T2Set3'] = "0"
            if "Tr1S4" in match:  
                match_to_process['T1Set4'] = match["Tr1S4"]
            else: match_to_process['T1Set4'] = "0"
            if "Tr2S4" in match:  
                match_to_process['T2Set4'] = match["Tr2S4"]
            else: match_to_process['T2Set4'] = "0"
            if "Tr1S5" in match:  
                match_to_process['T1Set5'] = match["Tr1S5"]
            else: match_to_process['T1Set5'] = "0"
            if "Tr2S5" in match:  
                match_to_process['T1Set5'] = match["Tr2S5"]
            else: match_to_process['T1Set5'] = "0"


            if "Eps" in match:  
                match_to_process['status'] = match["Eps"]
            else: match_to_process['status'] = "0"
            if "Ewt" in match:  
                match_to_process['winner'] = match["Ewt"]
            else: match_to_process['winner'] = "0"
            
            
            try:
                found_match = Match.objects.get(pk=match_to_process["match_id"])
            except Match.DoesNotExist:
                found_match = None

            #if the match is not in the db
            if found_match == None:
                #post new match
                serializer = MatchSerializer(data=match_to_process)
                if serializer.is_valid():
                    serializer.save()
                print(serializer.errors)
            else:
                #patch existing match
                serializer = MatchSerializer(found_match, data=match_to_process)
                if serializer.is_valid():
                    serializer.save()
                print(serializer.errors)
            

def list_by_date(request, date_string):
    
    # if request.user not isAdmin
        # raise PermissionDenied('You are not authorized to do that')
    
    url = "https://livescore6.p.rapidapi.com/matches/v2/list-by-date"
   
    #get todays date.now() and format it for the querystring
    # example date_strings: [2023][03][09]
    # 20230309
    # 20230310
    # 20230314

    querystring = {"Category":"tennis","Date":{date_string},"Timezone":"-7"}

    headers = {
        "X-RapidAPI-Key": "9b71ef6a10msh3f6d5e6bda5aa3ap1a62c2jsnf9ceb39aa5f4",
        "X-RapidAPI-Host": "livescore6.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    # use response data to update the stored match data
    update_stored(response.json())
    
    return JsonResponse(response.json(), safe=False)