from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate 

from .models import Account
from .serializers import AccountSerializer, RegistrationSerializer

SUCCESS = 'exito'
ERROR = 'error'
DELETE_SUCCESS = 'Eliminado'
UPDATE_SUCCESS = 'Actualizado'
CREATE_SUCCESS = 'Creado'

# Create your views here.

# Iniciar sesión
# Permite iniciar sesión en el sistema
# Url: http://159.89.50.94/login
@api_view(['POST',])
@permission_classes([AllowAny,])
def api_sing_up_account_view(request):
	if request.method == 'POST':
		data = {}
		account = authenticate(
		request, 
		username=request.POST.get('email'), 
		password=request.POST.get('password'))
	if account:
		try:
			token = Token.objects.get(user=account)
			data['response'] = 'Se ha ingresado'
			data['username'] = account.username
			data['email'] = account.email
			data['name'] = account.name
			data['token'] = token.key
			return Response(data, status=status.HTTP_201_CREATED)
		except Token.DoesNotExist:
			token = Token.objects.create(user=account)
	else:
		data['response'] = 'Error' 
		data['error_message'] = 'Datos inválidos'
		return Response(data)
	return Response(status=status.HTTP_400_BAD_REQUEST)

# Crea una cuenta
# Permite añadir una cuenta 
# Url: http://159.89.50.94/create
@api_view(['POST',])
@permission_classes([AllowAny,])
def api_create_account_view(request):
	if request.method == 'POST':
		serializer = RegistrationSerializer(data=request.data)
		data = {}
		if serializer.is_valid():
			account = serializer.save() 
			data['response'] = "se registró de forma exitosa"
			data['email'] = account.email
			data['username'] = account.username
			token = Token.objects.get(user = account).key
			data['token'] = token
			return Response(data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Obtiene propiedades de cuenta
# Obtiene las propiedades: name, email, username , estado, pic del objeto Account
# Url: https://159.89.50.94/peroperties
# Headers: Authorization: Token <token>
@api_view(['GET', ])
@permission_classes((IsAuthenticated,))
def api_detail_account_view(request):
	try:
		account = request.user
	except account.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
		
	if request.method == 'GET':
		serializer = AccountSerializer(account)
		return Response(serializer.data)	
