from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)
import googlemaps
from django.conf import settings

GOOGLE_MAPS_API_KEY = 'XXXXXXXX'

class Address(models.Model):
    addressLine1 = models.CharField(max_length=45)
    addressLine2 = models.CharField(max_length=45)
    suburbCity = models.CharField(max_length=45)
    country = models.CharField(max_length=45)
    stateProvince = models.CharField(max_length=45)
    zipCode = models.CharField(max_length=12)
    latitude = models.DecimalField(max_digits=14, decimal_places=12, blank=True, default='0')
    longitude = models.DecimalField(max_digits=15, decimal_places=12, blank=True, default='0')

    def __str__(self):
       return self.addressLine1 + " " + self.country

    def save(self, *args, **kwargs):
            location = "%s, %s, %s, %s, %s, %s" % (self.addressLine1, self.addressLine2, self.suburbCity, self.country, self.stateProvince, self.zipCode)
            gmaps_key = googlemaps.Client(key = GOOGLE_MAPS_API_KEY)
            geocode_result = gmaps_key.geocode(location)
            self.latitude = geocode_result[0]["geometry"]["location"]["lat"]
            self.longitude = geocode_result[0]["geometry"]["location"]["lng"]
            super(Address, self).save(*args, **kwargs)


class UserManager(BaseUserManager):
    def create_user(self, username, first_name, last_name, email, password=None):
        #if not email:
        #    raise ValueError("Users must have a email address")
        #if not password:
        #    raise ValueError("Users must have a password")
        user_obj = self.model(
            email = self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,

        )
        user_obj.set_password(password)
        user_obj.save(using=self._db)
        return user_obj

    def create_superuser(self, username, email, first_name, last_name,
    password=None):
        user = self.create_user(
            email = self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    username = models.CharField(max_length=15, unique=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='media', max_length=255,
    null=True, blank=True)
    address = models.ForeignKey(Address, null=True, on_delete=models.SET_NULL)
    #required fields
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login =  models.DateTimeField(verbose_name='last login', auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    objects = UserManager()

    def _str__(self):
        return self.username
    def has_perm(self, perm, obj=None):
        return self.is_admin
    def has_module_perms(self, app_label):
        return True

    def get_username(self):
        return self.username
    def get_latitude(self):
        return self.address.latitude
    def get_longitude(self):
        return self.address.longitude
