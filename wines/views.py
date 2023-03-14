from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
from  rest_framework import status
from  rest_framework.decorators import api_view
from  rest_framework.response import Response
# Create your views here.

@api_view(['GET','POST'])
def drink_list(request):

    if request.method=='GET':
        drinks=Drink.objects.all()
        serializer=DrinkSerializer(drinks,many=True)
        return JsonResponse(serializer.data,safe=False)
 
    if request.method =='POST':
        serializer=DrinkSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
@api_view(['GET','PUT','DELETE'])
def drink_detail(request,id):
    try:
    Drink.object.get(pk=id)
    
    except Drink.DoesnotExist:
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        pass
    elif request.method == 'DELETE':
        pass

