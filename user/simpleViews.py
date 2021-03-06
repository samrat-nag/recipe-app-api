from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
#from rest_framework.permissions import IsAuthenticatedOrReadOnly
""" without Authentication view only """
from rest_framework.permissions import IsAuthenticated
""" No authentication no View """

from user import simpleSirealizer
from user import models
from user import permission


class HelloApiView(APIView):
     serializer_class = simpleSirealizer.HelloSerializer

     def get(self, request , format=None):
         an_APIview = [
          'Uses HTTP test 1'
          'Uses HTTP test 2'
          'I am not a good Boy'
         ]
         return Response({'Message':'Hello!','Detail_msg':an_APIview})

     def post(self, request):
         serializer = self.serializer_class(data=request.data)

         if serializer.is_valid():
             name = serializer.validated_data.get('name')
             vmessage = f'Hello {name}'
             return Response({'message': vmessage})
         else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

     def put(self,request,pk=None):
          return Response({'msg-method':'PUT'})

     def patch(self,request,pk=None):
        return Response({'msg-method':'PATCH'})

     def delete(self,request,pk=None):
       return Response({'msg-method':'DELETE'})


class HelloViewSts(viewsets.ViewSet):
    serializer_class = simpleSirealizer.HelloSerializer

    def list(self,request):
        a_viewlist =[
            'Samrat'
            'good'
            'boy'
            ]
        return Response({'msg':'hello!','view_list':a_viewlist})


    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            vmessage = f'Hello {name}'
            return Response({'message': vmessage})
        else:
           return Response(
           serializer.errors,
           status=status.HTTP_400_BAD_REQUEST
           )

    def retrieve(self,request,pk=None):
             return Response({'http-method':'GET'})

    def update(self,request,pk=None):
           return Response({'http-method':'PUT'})

    def partial_update(self,request,pk=None):
           return Response({'http-method':'patch'})

    def destroy(self,request,pk=None):
          return Response({'http-method':'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = simpleSirealizer.UserProfileSerilizer
    queryset = get_user_model().objects.all()
    #queryset = models.userprofile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permission.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username','email',)


class UserLoginApiView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedVewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    serializer_class = simpleSirealizer.ProfileFeedItemSerializer
    queryset = models.UserProfileFeedItem.objects.all()
    permission_classes = {
               permission.UpdateOwnStatus,
               IsAuthenticated
    }

    def perform_create(self,serializer):
        serializer.save(username=self.request.user)
