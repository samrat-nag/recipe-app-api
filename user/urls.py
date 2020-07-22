from django.urls import path,include
from user import views,simpleViews
from rest_framework.routers import DefaultRouter



app_name ='user'

router =DefaultRouter()
router.register('hello-viewsets',simpleViews.HelloViewSts,basename='hello-viewsets')
router.register('profile-viewsets',simpleViews.UserProfileViewSet,basename='profile-viewsets')

urlpatterns = [
     path('create/', views.CreateUserView.as_view(),name='create'),
     path('token/', views.CreateTokenView.as_view(),name='token'),
     path('hello/', simpleViews.HelloApiView.as_view(),name='hello'),
     path('',include(router.urls)),


]
