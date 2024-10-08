from django.core.cache import cache
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from inventory_management_system.inventory.models import Inventory

from .serializers import InventorySerializer


class InventorryViewSet(ModelViewSet):
    serializer_class = InventorySerializer
    queryset = Inventory.objects.all()
    lookup_field = "pk"
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        cache_key = "inventory_data"  # Define cache key
        cached_inventory = cache.get(cache_key)
        if cached_inventory is None:
            queryset = self.filter_queryset(self.get_queryset())
            serializer = self.get_serializer(queryset, many=True)
            cached_inventory = serializer.data
            cache.set(cache_key, serializer.data, timeout=3600)
        return Response(cached_inventory)

    def create(self, request, *args, **kwargs):
        request_data = request.data.copy()
        request_data["created_by"] = request.user.pk
        serializer = self.get_serializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers,
        )
