from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.middleware.csrf import get_token

from ..models.watched_match import WatchedMatch
from ..serializers import WatchedMatchSerializer, WatchedMatchReadSerializer

# Create your views here.
class WatchedMatches(generics.ListCreateAPIView):
    """
    A view for creating and viewing all watched_matches

    /watched_matches/
    """
    queryset = ()
    serializer_class = WatchedMatchSerializer

    def get(self, request):
        """Index request"""
        watched_matches = WatchedMatch.objects.all()
        # .filter(owner = request.user)
        serializer = WatchedMatchReadSerializer(watched_matches, many=True)
        return Response(serializer.data)

    def post(self, request):
        """Post request"""
        serializer = WatchedMatchSerializer(data=request.data)
        if serializer.is_valid():
            m = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WatchedMatchDetail(generics.ListCreateAPIView):
    """
    A view for updating, viewing, and deleting a single watched_match

    /watched_matches/<int:pk>
    """
    serializer_class = WatchedMatchSerializer

    def get(self, request, pk):
        """Show request"""
        match = get_object_or_404(WatchedMatch, pk=pk)

        #does the user own the match?
        # if request.user != match.owner:
        #     raise PermissionDenied('You do no own this match')

        serializer = WatchedMatchSerializer(match)
        return Response(serializer.data)

    def delete(self, request, pk):
        """Delete request"""
        match = get_object_or_404(WatchedMatch, pk=pk)

        # if request.user != match.owner:
        #     raise PermissionDenied('You do no own this match')

        match.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk):
        """Update Request"""
        match = get_object_or_404(WatchedMatch, pk=pk)

        # if request.user != match.owner:
        #     raise PermissionDenied('You do no own this match')

        # #why do we need this step....
        # request.data['match']['owner'] = request.user.id

        # Validate updates with serializer
        serializer = WatchedMatchSerializer(match, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)