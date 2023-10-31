from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import status, generics
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user, authenticate, login, logout

from ..serializers import UserSerializer, UserRegisterSerializer
from ..models.user import User

class SignUp(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserRegisterSerializer

    def post(self, request):
        user = UserRegisterSerializer(data=request.data)
        if user.is_valid():
            created_user = UserSerializer(data=user.data)
            if created_user.is_valid():
                created_user.save()
                return Response({ 'user': created_user.data }, status=status.HTTP_201_CREATED)
            else:
                return Response(created_user.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)

class SignIn(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer

    def post(self, request):
        creds = request.data
        user = authenticate(request, email=creds['email'], password=creds['password'])

        if user is not None:
            if user.is_active:
                login(request, user)
                return Response({
                    'user': {
                        'id': user.id,
                        'email': user.email,
                        'token': user.get_auth_token()
                    }
                })
            else:
                return Response({ 'msg': 'The account is inactive.' }, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({ 'msg': 'The username and/or password is incorrect.' }, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class SignOut(generics.DestroyAPIView):
    def delete(self, request): 
        request.user.delete_token()
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)
    


# view to check if a token is valid

class IsValid(generics.RetrieveAPIView):
    def get(self, request):
        print("checking if user is valid")