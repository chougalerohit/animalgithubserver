from rest_framework import serializers
from .models import cow_info_model



class cow_serializer(serializers.ModelSerializer):
    class Meta:
        model = cow_info_model
        fields = '__all__'