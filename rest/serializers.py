from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    firstname = serializers.CharField(max_length=10)
    # lastname = serializers.CharField(max_length=1)




