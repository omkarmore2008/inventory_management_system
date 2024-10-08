from rest_framework import serializers

from inventory_management_system.inventory.models import Inventory


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = "__all__"
