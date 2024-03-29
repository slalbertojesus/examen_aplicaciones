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
			estado=self.validated_data['estado'],
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


class AccountLoginSerializer(serializers.ModelSerializer):
	class Meta:
		model = Account
		fields = ['name', 'email', 'username', 'estado']