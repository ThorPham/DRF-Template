from django.db import models
import uuid
from app.models.account import Account

class Supporter(models.Model):
   id = models.UUIDField(primary_key=True, default=uuid.uuid4)
   account_id = models.ForeignKey(Account,on_delete=models.CASCADE)
   is_online = models.BooleanField(default=False)