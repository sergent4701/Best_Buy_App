from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import RegexValidator


class UserManager(BaseUserManager):
    list_display = ('username', 'full_name', 'is_admin')
    def create_user(self, username, full_name, password=None): # Required fields
        if not username:
            raise ValueError("Users must have an username")
        if not full_name:
            raise ValueError("Users must have a full name")
        user = self.model(
            username=username,
            full_name=full_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, full_name, password=None):
        user = self.create_user(
            username=username,
            password=password,
            full_name=full_name,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    MANAGER = 'MA'
    PCHO = 'PC'
    APPLIANCES = 'AP'
    HOME_THEATER = 'HT'
    MOBILE = 'MO'
    CONNECTED_HOME = 'CH'
    FRONT_LANE = "FL"
    employee_type_choices = [
        (MANAGER, 'Manager'),
        (PCHO, 'PCHO'),
        (APPLIANCES, 'Appliances'),
        (HOME_THEATER, 'Home Theater'),
        (MOBILE, 'Mobile'),
        (CONNECTED_HOME, 'Connected Home'),
        (FRONT_LANE, 'Front Lane'),
    ]
    numeric = RegexValidator(r'^[0-9]*$', 'Only numeric characters are allowed.')

    username = models.CharField(max_length=7, blank=True, null=True, validators=[numeric], unique=True)
    full_name = models.CharField(max_length=255)
    employee_type = models.CharField(max_length=2, choices=employee_type_choices, default=MANAGER)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    # Username_Field and Password are required by default
    REQUIRED_FIELDS = ['full_name']

    objects = UserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True