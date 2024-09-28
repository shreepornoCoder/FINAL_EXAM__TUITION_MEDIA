from rest_framework import serializers
from .models import UserTuitionHistory

class Tuition_History_Serializer(serializers.ModelSerializer):
    class Meta:
        model = UserTuitionHistory
        exclude = ["time"]