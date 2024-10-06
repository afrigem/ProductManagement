from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated 
from django_filters.rest_framework import DjangoFilterBackend
from products.models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'price', 'stock']
    search_fields = ['name', 'category__name']
    ordering_fields = ['price', 'created_at']

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
