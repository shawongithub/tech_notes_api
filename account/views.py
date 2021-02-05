from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from account.serializers import SignupSerializer
from rest_framework.authtoken.models import Token

@api_view(['POST'])
def signup(request):
   
    if request.method == 'POST':
        serializer=SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

