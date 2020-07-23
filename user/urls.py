from django.urls import path,include
from user import views,simpleViews
from rest_framework.routers import DefaultRouter



app_name ='user'

router =DefaultRouter()
router.register('hello-viewsets',simpleViews.HelloViewSts,basename='hello-viewsets')
router.register('profile-viewsets',simpleViews.UserProfileViewSet,basename='profile-viewsets')
router.register('feed',simpleViews.UserProfileFeedVewSet,basename='profile-feed')

urlpatterns = [
     path('create/', views.CreateUserView.as_view(),name='create'),
     path('token/', views.CreateTokenView.as_view(),name='token'),
     path('hello/', simpleViews.HelloApiView.as_view(),name='hello'),
     path('login/',simpleViews.UserLoginApiView.as_view()),
     path('',include(router.urls)),


]
