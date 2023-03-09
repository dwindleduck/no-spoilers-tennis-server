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

    def post(self, request):
        """Post request"""
        serializer = MatchSerializer(data=request.data)
        if serializer.is_valid():
            m = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MatchDetail(generics.ListCreateAPIView):
    """
    A view for updating, viewing, and deleting a single match

    /matches/<int:pk>
    """
    serializer_class = MatchSerializer

    def get(self, request, pk):
        """Show request"""
        match = get_object_or_404(Match, pk=pk)

        #does the user own the match?
        # if request.user != match.owner:
        #     raise PermissionDenied('You do no own this match')

        serializer = MatchSerializer(match)
        return Response(serializer.data)

    def delete(self, request, pk):
        """Delete request"""
        match = get_object_or_404(Match, pk=pk)

        # if request.user != match.owner:
        #     raise PermissionDenied('You do no own this match')

        match.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk):
        """Update Request"""
        match = get_object_or_404(Match, pk=pk)

        # if request.user != match.owner:
        #     raise PermissionDenied('You do no own this match')

        # #why do we need this step....
        # request.data['match']['owner'] = request.user.id

        # Validate updates with serializer
        serializer = MatchSerializer(match, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)