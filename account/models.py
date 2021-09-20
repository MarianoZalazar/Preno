from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class MyAccountManager(BaseUserManager):
    def create_user(self, email, cargo, nombre_apellido, password=None):
        if not email:
            raise ValueError('Los usuarios necesitan un correo electronico')
        user = self.model(email=self.normalize_email(email), 
                            cargo=cargo.capitalize(), 
                            nombre_apellido=nombre_apellido.title())

        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_superuser(self, email, cargo, nombre_apellido, password):
        user = self.create_user(email=self.normalize_email(email), cargo=cargo, nombre_apellido=nombre_apellido, password=password)

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        
        user.save(using=self._db)

        return user


class Account(AbstractBaseUser):
    email = models.EmailField(max_length=100, unique=True)
    nombre_apellido = models.CharField(max_length=150)
    cargo = models.CharField(max_length=50)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre_apellido', 'cargo']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


# Create your models here.