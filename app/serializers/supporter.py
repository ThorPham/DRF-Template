from rest_framework import serializers
from app.models import Account, Supporter

class SupporterSerializer(serializers.ModelSerializer):
   class Meta:
      model = Supporter
      fields = "__all__"

   def validate_account_id(self, value):
      if not Account.objects.filter(id=value.id).exists():
         raise serializers.ValidationError("The account does not exist.")
      return value