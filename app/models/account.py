from django.db import models
import uuid
from phonenumber_field.modelfields import PhoneNumberField 

class Account(models.Model):
   id = models.UUIDField(primary_key=True, default=uuid.uuid4)
   full_name = models.CharField(max_length=255)
   phone_number = PhoneNumberField(blank=False)
   password = models.CharField(max_length=128)
   is_active = models.BooleanField(default=False)
   is_superuser = models.BooleanField(default=False)
   is_verified = models.BooleanField(default=False)

   def __str__(self) -> str:
      return self.full_name + " | " + str(self.phone_number)