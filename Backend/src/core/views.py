

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer, UserDataSerializerGet, UserDataSerializerInsert
from .models import UserData, User



class SignUp(APIView):
    permission_classes = (AllowAny,)
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            User.objects.create_user(
                username = request.data["email"],
                email=request.data["email"],
                password=request.data["password"],
                first_name=request.data["first_name"],
                last_name=request.data["last_name"]
            )
            return Response(serializer.data)
        return Response(serializer.errors)



class InsertUserData(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
        serializer = UserDataSerializerInsert(data=request.data)
        # print(serializer.data, type(serializer.data))
        if serializer.is_valid():
            ob = UserData.objects.create(
                name = request.data["name"],
                amount=request.data["amount"],
                cashflow=request.data["cashflow"],
                category=request.data["category"],
                interval=request.data["interval"],
                description=request.data["description"],
                owner=request.user
            )
            return Response(ob.pk)
        return Response(serializer.errors)



class DeleteUserData(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
        UserData.objects.filter(id=request.data["id"]).delete()
        return Response({"deletedpk":request.data["id"]})



class EditUserData(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
        serializer = UserDataSerializerGet(data=request.data)
        # print(serializer.data, type(serializer.data))
        if serializer.is_valid():
            UserData.objects.filter(id=request.data["id"]).update(
                name = request.data["name"],
                amount=request.data["amount"],
                cashflow=request.data["cashflow"],
                category=request.data["category"],
                interval=request.data["interval"],
                description=request.data["description"]
            )
            ob = UserData.objects.get(pk=request.data["id"])
            return Response(ob.pk)
        return Response(serializer.errors)



class GetUserData(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        qs = UserData.objects.filter(owner=request.user)
        serializer = UserDataSerializerGet(qs, many = True)
        # print(serializer.data)
        return Response(serializer.data)



class Analysis(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        return Response(data={"message" : "Under Construction"})
    def timeseries(self):
        pass
    def sentimentalanalysis(self):
        pass
    