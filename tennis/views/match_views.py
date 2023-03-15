from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.middleware.csrf import get_token

from ..models.match import Match
from ..serializers import MatchSerializer

# Create your views here.
class Matches(generics.ListCreateAPIView):
    """
    A view for creating and viewing all matches

    /matches/
    """
    queryset = ()
    serializer_class = MatchSerializer

    def get(self, request):
        """Index request"""
        matches = Match.objects.all()
        # .filter(owner = request.user)
        serializer = MatchSerializer(matches, many=True)
        return Response(serializer.data)
