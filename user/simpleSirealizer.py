from rest_framework import serializers
from django.contrib.auth import get_user_model
from user import models

class  HelloSerializer(serializers.Serializer):
       name = serializers.CharField(max_length=10)


class UserProfileSerilizer(serializers.ModelSerializer):

     class Meta:
         model = get_user_model()
         #model = models.userprofile
         fields = ('email','password','username')
         extra_kwargs ={
         'password':{'write_only': True,
                     'min_length':5,
                     'style':{'input_type':'password'}
           }
         }

         def create(self,validated_data):
             user = get_user_model().objects.create_user(
             #user=    models.userprofile.objects.create_user(
                email = validated_data['email'],
                username = validated_data['name'],
                password = validated_data['password']
             )
             return user


class ProfileFeedItemSerializer(serializers.ModelSerializer):

      class Meta:
          model = models.UserProfileFeedItem
          fields =('id','username','ACC_class','status_text','created_on')
          extra_kwargs = {'username': {'read_only':True}}
