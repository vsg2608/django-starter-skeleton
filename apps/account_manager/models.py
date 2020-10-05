from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import (
    BaseUserManager as BUM,
    PermissionsMixin,
    AbstractBaseUser
)

from apps.common.models import BaseModel

class Account(BaseModel):
    id          = models.AutoField(verbose_name="ID", primary_key= True)
    name        = models.CharField( verbose_name="Name", max_length= 255, unique=True, null=False, blank= False)
    billingAddress = models.TextField(verbose_name="Billing Address", null= True, blank= True)
    isActive    = models.BooleanField(verbose_name="Active", default= True, blank= False, null= False)
    #icon        = models.ImageField(verbose_name="Active", upload_to=None, height_field=None, width_field=None, max_length=None)
    website     = models.CharField( verbose_name="Website", max_length= 255, unique=False, null=True, blank= True)
    description = models.TextField(verbose_name="Description", null= True, blank= True)
     
    class Meta:
        verbose_name = _("Account")
        verbose_name_plural = _("Accounts")

    def __str__(self):
        return self.name
    
class Profile(BaseModel):
    id          = models.AutoField(verbose_name="ID", primary_key= True)
    name        = models.CharField( verbose_name="Name", max_length= 144, unique=True, null=False, blank= False)
     
    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")

    def __str__(self):
        return self.name

class BaseUserManager(BUM):
    def create_user(self, email, username, is_active=True, is_admin=False, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have an username')

        user = self.model(
            email=self.normalize_email(email.lower()),
            username= username,
            is_active=is_active,
            is_admin=is_admin
        )

        if password is not None:
            user.set_password(password)
        else:
            user.set_unusable_password()

        user.full_clean()
        user.save(using=self._db)

        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(
            email=email,
            username= username,
            is_active=True,
            is_admin=True,
            password=password,
        )

        user.is_superuser = True
        user.save(using=self._db)

        return user


class BaseUser(BaseModel, AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    username= models.CharField(verbose_name='Username', max_length=255, unique= True)
    first_name= models.CharField(verbose_name='First Name', max_length=255, null=True)
    last_name= models.CharField(verbose_name='Last Name', max_length=255, null=True)
    account= models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank= False)
    profile= models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank= False)
   
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = BaseUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS= ['username']

    def __str__(self):
        return self.email

    def is_staff(self):
        return self.is_admin

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")