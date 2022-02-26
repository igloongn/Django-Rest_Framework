from django.shortcuts import redirect, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest import serializers

def index(request):
    return redirect('first')









class HelloApiview(APIView):
    ser_class=serializers.HelloSerializer

    def get(self, request, format=None):
        p={}
        p['msg']="Hello World"
        p['class']="400 level"
        p['dept']="Computer Science"
        return Response(p)

    def post(self, request, format=None):
        p={}
        ser=self.ser_class(data=request.data)
        if ser.is_valid():
            firstname=ser.validated_data.get('firstname')
            lastname=ser.validated_data['lastname']
            message=f"Hello {firstname}-{lastname}"
            p['message']=message
            return Response(p)
        else:
            p['error']=ser.errors
            p['status']=status.HTTP_400_BAD_REQUEST
            return Response(p)
            
    def put(self, request, pk=None):
        p={}

        p['msg']="This is a PUT"
        return Response(p)

    def patch(self, request, pk=None):
        p={}
        
        p['msg']="This is a PATCH"
        return Response(p)
    def delete(self, request, pk=None):
        p={}

        p['msg']="This is a DELETE"
        return Response(p)
        
        


