from django.shortcuts import render

# Create your views here.

# Iniciar sesión
# Permite iniciar sesión en el sistema
# Url: http://merixo.tk/login
@api_view(['POST',])
@permission_classes([AllowAny,])
def api_sing_up_usuario_view(request):
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
			data['estado'] = account.estado
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
# Url: http://merixo.tk/create
@api_view(['POST',])
@permission_classes([AllowAny,])
def api_create_usuario_view(request):
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