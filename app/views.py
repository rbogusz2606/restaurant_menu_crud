from .models import Menu
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import MenuSerializer

@api_view(['GET', 'POST'])
def MenuList(request):

    if request.method == 'GET':
        menu = Menu.objects.all()
        serializer = MenuSerializer(menu, many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET', 'PUT', 'DELETE'])
def Show_Change_Delete_Obj(request, id):

    try:
        object = Menu.objects.get(pk=id)
    except Menu.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = MenuSerializer(object)
        return Response(serializer.data)


    elif request.method == 'PUT':
        serializer = MenuSerializer(object,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  