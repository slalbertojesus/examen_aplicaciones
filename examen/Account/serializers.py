import os
from rest_framework import serializers
from django.db import models
from .models import Account
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.storage import FileSystemStorage

IMAGE_SIZE_MAX_BYTES = 1024 * 1024 * 2 # 2MB
MIN_TITLE_LENGTH = 5
MIN_BODY_LENGTH = 50

class RegistrationSerializer(serializers.ModelSerializer):

	passwordConfirm = serializers.CharField(style={'input_type': 'password'}, write_only=True)

	class Meta:
		model = Account
		fields = ['email', 'username', 'password', 'passwordConfirm', 'name']
		extra_kwargs = {
				'password': {'write_only': True},
		}	

	def update(self, instance, validated_data):
		account = Account(
			email=self.validated_data['email'],
			username=self.validated_data['username'],
			name=self.validated_data['name'],
			)
		if RegistrationSerializer.is_valid():
			RegistrationSerializer.update(instance=instance.account)
		return super(RegistrationSerializer, self).update(instance, validated_data)

	def	save(self):
		account = Account(
			email=self.validated_data['email'],
			username=self.validated_data['username'],
			name=self.validated_data['name'],
			)
		password = self.validated_data['password']
		passwordConfirm = self.validated_data['passwordConfirm']
		if password != passwordConfirm:
			raise serializers.ValidationError({'password': 'Contraseñas no son iguales.'})
		account.set_password(password)
		account.save()
		return account


class AccountSerializer(serializers.ModelSerializer):
	class Meta:
		model = Account
		fields = ['name', 'email']

	def	save(self):
		account = Account(
			email=self.validated_data['email'],
			username=self.validated_data['username'],
			name=self.validated_data['name'],
			)
		account.save()
		return account
