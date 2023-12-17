from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth import get_user_model
from django.utils import timezone


# User Manager
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user"""
        if not email:
            raise ValueError('User must have an email address.')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None):
        """For creating a superuser or an admin user which is going to have the access for django admin panel."""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    """
    User in the system
    """
    email = models.EmailField(max_length=100, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    objects = UserManager()


def user_image_upload_path(instance, filename):
    # Assuming the user's name is stored in a field called 'name'
    filename = 'profile_pic.jpeg'
    return f'profile/{instance.user.email}/{filename}'


def user_aadhar_upload_path(instance, filename):
    # Assuming the user's name is stored in a field called 'name'
    return f'aadhar/{instance.user.email}/{filename}'


def user_pan_upload_path(instance, filename):
    # Assuming the user's name is stored in a field called 'name'
    return f'pan/{instance.user.email}/{filename}'


class Detail(models.Model):
    e_id = models.AutoField(primary_key=True, auto_created=True, serialize=False)
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=252)
    aadhar_no = models.CharField(max_length=12)
    pan_no = models.CharField(max_length=10)
    profile_pic = models.ImageField(upload_to=user_image_upload_path, null=True, blank=True, )
    aadhar_file = models.FileField(upload_to=user_aadhar_upload_path, null=True, blank=True, )
    pan_file = models.FileField(upload_to=user_pan_upload_path, null=True, blank=True, )
    blood_group = models.CharField(max_length=5)
    designation = models.CharField(max_length=200, null=True, blank=True)
    employee_code = models.CharField(max_length=255, null=True, editable=False)
    date_of_birth = models.DateField(null=True, blank=True)
    current_package = models.IntegerField(null=True, blank=True)
    monthly_income = models.IntegerField(null=True, blank=True)
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, blank=True)
    MARITIAL_CHOICES = [
        ('married', 'Married'),
        ('single', 'Single'),
        ('divorced', 'Divorced')
    ]
    marital_status = models.CharField(max_length=10, choices=MARITIAL_CHOICES, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)

        # Set the employee_code based on e_id after saving
        self.employee_code = f'emp{str(self.e_id).zfill(4)}'
        super().save(update_fields=['employee_code'], *args, **kwargs)

    def __str__(self):
        return f'User: {self.user.name}'
