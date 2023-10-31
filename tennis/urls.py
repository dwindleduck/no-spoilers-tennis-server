from django.urls import path
from .views.match_views import Matches
from .views.watched_matches_views import WatchedMatches, WatchedMatchDetail
from .views.create_and_get import create_and_get_cards
from .views.user_views import SignUp, SignIn, SignOut, IsValid

urlpatterns = [
  	# Restful routing
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    # path('is-valid/', IsValid.as_view(), name='is-valid'),

    path('matches/<str:date>/', Matches.as_view(), name='matches_by_date'),

    path('watched_matches/', WatchedMatches.as_view(), name='watched_matches'),
    path('watched_matches/<int:pk>/', WatchedMatchDetail.as_view(), name='watched_match_detail'),
    path('watched_matches/create_and_get/<str:date>/', create_and_get_cards),
    
]