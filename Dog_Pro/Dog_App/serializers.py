# from django import serializers
from Dog_App.models import Dog
from rest_framework import serializers

class DogSerializer(serializers.ModelSerializer):
    image =serializers.ImageField(max_length=None, use_url=True)
    doc =serializers.FileField(max_length=None, use_url=True)
    class Meta:
        model = Dog
        fields = ['name' , 'color', 'image','doc']