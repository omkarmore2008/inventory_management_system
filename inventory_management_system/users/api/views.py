from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from inventory_management_system.users.models import User

from .serializers import UserCreateSerializer
from .serializers import UserSerializer


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "pk"
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == "create":
            return UserCreateSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action == "create":
            return [AllowAny()]
        return super().get_permissions()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers,
        )
