from django.contrib.auth import logout
from rest_framework.authtoken.models import Token
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, CreateAPIView, ListAPIView
from .models import Message, User
from .serializers import MessageSerializer, RegistrationSerializer
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.response import Response


class Logout(ListAPIView):
    def get(self, request, *args, **kwargs):
        try:
            request.user.auth_token.delete()
        except:
            return Response('error')
        logout(request)
        return Response('logout')


class Login(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = RegistrationSerializer(data=request.data)
        if not serializer.is_valid():
            return Response('Все плохо')
        user = serializer.validated_data
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response({'errors': serializer.errors})


class Register(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.create(user=user)
            return Response({'token': token.key})
        return Response({'errors': serializer.errors})


class MessageList(ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MessageUpdate(RetrieveUpdateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAdminUser]


class MessageDestroy(RetrieveDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer