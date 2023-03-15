from django.urls import path
from .views.match_views import Matches
from .views.watched_matches_views import WatchedMatches, WatchedMatchDetail
from .views.user_views import SignUp, SignIn, SignOut

from .LiveScore_Requests import list_by_date

urlpatterns = [
  	# Restful routing
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('matches/', Matches.as_view(), name='matches'),
    path('watched_matches/', WatchedMatches.as_view(), name='watched_matches'),
    path('watched_matches/<int:pk>/', WatchedMatchDetail.as_view(), name='watched_match_detail'),
    
    # LiveScore API call
    path('list_by_date/<int:date_string>', list_by_date),
]