from django.db import models

class Account(AbstractBaseUser):
	name                    = models.CharField(max_length=30)
	email 					= models.EmailField(max_length=60, unique=True)
	username 				= models.CharField(max_length=30, unique=True)

    USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']

    def __str__(self):
		return self.email

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)