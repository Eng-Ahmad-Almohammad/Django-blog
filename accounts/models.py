from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.shortcuts import reverse

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(
        self, email, first_name, last_name, password=None, **other_fields
    ):
        if not email:
            raise ValueError("You must provide an email address")

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            **other_fields,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self, email, first_name, last_name, password=None, **other_fields
    ):
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_active", True)
        if other_fields.get("is_staff") is not True:
            raise ValueError("Superuser must be assigned to is_staff=True")

        if other_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must be assigned to is_superuser=True")

        return self.create_user(
            email, first_name, last_name,  password, **other_fields
        )



class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
        blank=False,
        null=False,
        max_length=256

    )

    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse('login')

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'