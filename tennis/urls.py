from django.urls import path
from .views.match_views import Matches, MatchDetail
#RefreshMatches
from .views.watched_matches_views import WatchedMatches, WatchedMatchDetail
from .views.user_views import SignUp, SignIn, SignOut

from .LiveScore_Requests import list_by_date, competition_detail

urlpatterns = [
  	# Restful routing
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('matches/', Matches.as_view(), name='matches'),
    path('matches/<int:pk>/', MatchDetail.as_view(), name='match_detail'),
    path('watched_matches/', WatchedMatches.as_view(), name='watched_matches'),
    path('watched_matches/<int:pk>/', WatchedMatchDetail.as_view(), name='watched_match_detail'),
    
    # LiveScore API calls
    # path('refresh/list_by_date/', RefreshMatches.as_view(), name='refresh-by-date'),
    path('list_by_date/', list_by_date),
    # path('competition_detail', competition_detail)
]