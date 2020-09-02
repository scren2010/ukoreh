from django.contrib.auth import get_user_model
from django.http import Http404
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.userprofile.models import Profile
from backend.userprofile.serializers import UserSerializer, ProfileSerializer
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

def social_login(self, request):
    user = request.user
    token = SocialToken.objects.filter(account__user=user, account__provider='google')
    print('привет!')
    print(user)
    print(token)
    return Response('КУКУ')