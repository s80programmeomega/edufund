from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.models import (AbstractBaseUser, AnonymousUser,
                                        BaseUserManager, PermissionsMixin)
from django.db import models


class UserType(models.TextChoices):
    GUEST = "GUEST", "Guest"
    SCHOOL = 'SCHOOL', 'School'
    SPONSOR = 'SPONSOR', 'Sponsor'
    ADMIN = 'ADMIN', 'Admin'


class CustomUserManager(BaseUserManager):
    """Define a model manager for CustomUser model with no username field."""

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):

        extra_fields.setdefault('user_type', UserType.ADMIN)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """Custom user model with email as the unique identifier.
    """

    user_type = models.CharField(
        max_length=20,
        choices=UserType.choices,
        default=UserType.GUEST
    )

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'user_type']

    def save(self, *args, **kwargs):
        # Set the admin status according to the user type
        if self.user_type == UserType.ADMIN:
            self.is_superuser = True
            self.is_staff = True
        else:
            self.is_superuser = False
            self.is_staff = False

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.email


class CustomAnonymousUser(AnonymousUser):
    def __init__(self):
        super().__init__()
        self._user_type = "Guest"

    @property
    def user_type(self):
        return self._user_type

    @user_type.setter
    def user_type(self, value):
        self._user_type = value
