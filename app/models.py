from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
# Create your models here.



class UserProfileManager(BaseUserManager):
    def create_user(self,email,first_name,last_name,password=None):
        if not email:
            raise ValueError('please provide email ')
        nrml_em=self.normalize_email(email)
        uo=self.model(email=nrml_em,first_name=first_name,last_name=last_name)
        uo.set_password(password)
        uo.save()
        return uo
    
    def create_superuser(self,email,first_name,last_name,password):
        uo=self.create_user(email,first_name,last_name,password)
        uo.is_staff=True
        uo.is_superuser=True
        uo.save()



class UserProfile(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(max_length=50,primary_key=True)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['first_name','last_name']
    objects=UserProfileManager()