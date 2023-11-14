# from django.contrib.auth.models import User
# from django.contrib.auth.password_validation import validate_password
# from django.contrib.auth import authenticate
# from rest_framework import serializers
# from rest_framework.authtoken.models import Token
# from rest_framework.validators import UniqueValidator

from rest_framework import serializers
from .models import UserProfile

from .models import classlist, UserClasslist


# class RegisterSerializer(serializers.ModelSerializer):
#     id = serializers.CharField(required=True, validators=[
#                                UniqueValidator(queryset=User.objects.all())])
#     pw = serializers.CharField(
#         write_only=True, required=True, validators=[validate_password])
#     pw2 = serializers.CharField(write_only=True, required=True)

#     class Meta:
#         model = User
#         fields = ['username', 'id', 'pw', 'pw2']

#     def validate(self, data):
#         if data['pw'] != data['pw2']:
#             raise serializers.ValidationError(
#                 {"pw": "Password fields didn't match."})
#         return data

#     def create(self, validated_data):
#         student = User.objects.create_user(
#             id=validated_data['id'], username=validated_data['username'])
#         student.set_password(validated_data['pw'])
#         student.save()
#         token = Token.objects.create(user=student)

#         return student


# class LoginSerializer(serializers.Serializer):
#     username = serializers.CharField(required=True)
#     password = serializers.CharField(required=True, write_only=True)

#     def validate(self, data):
#         user = authenticate(**data)
#         if user:
#             token = Token.objects.get(user=user)
#             return token
#         raise serializers.ValidationError(
#             {"error": "Unable to log in with provided credentials."})


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['student_id', 'name']


class classserializer(serializers.ModelSerializer):
    class Meta:
        model = classlist
        fields = ['id', 'name', 'professor', 'day1', 'day2', 'starttime1',
                  'endtime1', 'starttime2', 'endtime2', 'place', 'major']


# class CSVFileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CSVFile
#         fields = ('id', 'file', 'uploaded_at')

class ClassPickSerializer(serializers.ModelSerializer):
    class Meta:
        model = classlist
        fields = ['id', 'name']

class UserClasslistSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserClasslist
        fields = ['user', 'userclass']