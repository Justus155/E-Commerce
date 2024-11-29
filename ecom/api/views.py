from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Product
from  .serializer import ProductSerializer

#POST /products: Creates a new product with the data sent in the request body, and returns the new product as JSON.
class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    from rest_framework import generics, status
from rest_framework.response import Response
from .models import Product


class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#GET /products: Retrieves a list of all products as JSON.
class ProductRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

def homepage(request):
    return render(request, 'home.html')
    # return render(request, 'templates/home.html')

