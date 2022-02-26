from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    firstname = serializers.CharField(max_length=10, allow_null=True, default="This is the firstname")
    lastname = serializers.CharField(max_length=10, default="This is the firstname")




