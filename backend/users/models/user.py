from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
class Admin(BaseUserManager):
    def create_user(self, username, password=None):
        """
        Creates and saves a User with the given username, password 
        birth and password.
        """
        user = self.model(
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            username = username,
            password = password,
            
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    """ esta es la documentacion de la clase User: 
    la clase user es un modelo personalizado del usuario django 
    """
    id = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=250)
    email = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    money = models.IntegerField(default=0)
    fbid = models.CharField(max_length=150, blank=True)
    first_name = models.CharField(max_length=32, blank=True)
    last_name = models.CharField(max_length=32, blank=True)
    uid = models.CharField(max_length=150, blank=True, null=True)
    regtime = models.DateTimeField(default=now, blank=True)
    last_login = models.DateTimeField('last_login', blank=True, null=True)
    modtime = models.DateTimeField(default=now, blank=True)
    phone = models.CharField(max_length=32, blank=True, null=True)
    device = models.CharField(max_length=32, blank=True, null=True)
    ip = models.CharField(max_length=32, blank=True, null=True)
    country = models.CharField(max_length=32, blank=True, null=True)
    mac = models.CharField(max_length=32, blank=True, null=True)
    ctrlcode = models.SmallIntegerField(db_column='CtrlCode', blank=True, null=True)  # Field name made lowercase.
    invitecode = models.CharField(max_length=6, blank=True, null=True)
    referrercode = models.CharField(max_length=6, blank=True, null=True)
    referralrebate = models.IntegerField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_merchant = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = Admin()
    LAST_LOGIN_FIELD = 'last_login'
    PASSWORD_FIELD = 'password'
    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        # The user is identified by their email address
        return self.username

    def get_short_name(self):
        # The user is identified by their email address
        return self.username

    def __str__(self):              # __unicode__ on Python 2
        return self.username

    def has_perm(self):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    class Meta:
        managed = True
        db_table = 't_users'
        verbose_name = "User"
        verbose_name_plural = "Users"
        app_label= "users"