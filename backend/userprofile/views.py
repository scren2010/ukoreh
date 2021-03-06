from django.contrib.auth import get_user_model
from django.http import Http404
from rest_auth import serializers
from rest_auth.models import TokenModel
from rest_framework.authtoken.models import Token
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.userprofile.models import Profile
from backend.userprofile.serializers import UserSerializer, ProfileSerializer, TokenSerializer
from backend.userprofile.permissions import IsOwnerOrReadOnly

User = get_user_model()


class UserView(APIView):
    """ Получить пользователя """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        ser = UserSerializer(User.objects.get(id=request.user.id))
        return Response(ser.data)


class UpdateUserView(APIView):
    """ Обновить имя пользователя """
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = UserSerializer
    """
     Retrieve, update or delete a snippet instance.
     """
    def put(self, request):
        user = User.objects.get(id=request.user.id)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ProfileView(APIView):
    """ Получить профиль пользователя """
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get(self, request):
        ser = ProfileSerializer(Profile.objects.get(user=request.user))
        return Response(ser.data)


from allauth.socialaccount.models import SocialToken

#
#
# class TakeToken(APIView):
#     permission_classes = [IsOwnerOrReadOnly]
#     def get(self, request):
#         user = request.user
#         if SocialToken.objects.filter(account__user=user, account__provider='google'):
#             token = SocialToken.objects.filter(account__user=user, account__provider='google')
#             ser = TokenSerializer(token[0])
#             return Response(ser.data)
#         else:
#             token = Token.objects.filter(user=user)
#             ser =  serializers.TokenSerializer(token[0])
#             return Response(ser.data)

