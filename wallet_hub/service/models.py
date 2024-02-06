from django.contrib.auth import get_user_model
from django.db import models


class TextDetail(models.Model):
    """
    Logged In User
    """
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, editable=False)
    """
    Details in Text
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    aadhar_no = models.CharField(max_length=12, null=True, blank=True)
    pan_no = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return f'Name: {self.first_name} {self.last_name}'
