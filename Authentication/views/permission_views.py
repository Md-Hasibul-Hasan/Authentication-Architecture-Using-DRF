from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission

from rest_framework import mixins, viewsets
from rest_framework.viewsets import (
    ReadOnlyModelViewSet,
    ModelViewSet
)


from rest_framework.permissions import  IsAdminUser
from Authentication.authentication import SessionJWTAuthentication
from ..renderers import UserRenderer

from drf_spectacular.utils import extend_schema

from ..serializers import (
    PermissionSerializer,
    GroupSerializer,
    UserGroupPermissionSerializer
)

from ..paginations import MyPageNumberPagination

User = get_user_model()


# ======================================================
# Permissions
# ======================================================
@extend_schema(tags=["Groups &  Permissions"])
class PermissionViewSet(ReadOnlyModelViewSet):
    queryset = (
        Permission.objects
        .all()
        .select_related("content_type")
        .order_by(
            "content_type__app_label",
            "codename"
        )
    )

    serializer_class = PermissionSerializer
    renderer_classes = [UserRenderer]
    permission_classes = [IsAdminUser]
    authentication_classes = [SessionJWTAuthentication]

    pagination_class = MyPageNumberPagination


# ======================================================
# Groups &  Permissions
# ======================================================

@extend_schema(tags=["Groups &  Permissions"])

class GroupViewSet(ModelViewSet):
    queryset = (
        Group.objects
        .all()
        .prefetch_related("permissions")
        .order_by("name")
    )

    serializer_class = GroupSerializer
    renderer_classes = [UserRenderer]
    permission_classes = [IsAdminUser]
    authentication_classes = [SessionJWTAuthentication]


# ======================================================
# User Group & Permissions
# ======================================================
@extend_schema(tags=["Groups &  Permissions"])

class UserGroupPermissionViewSet(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    queryset = (
        User.objects
        .all()
        .prefetch_related(
            "groups",
            "groups__permissions",
            "user_permissions",
        )
    )

    serializer_class = UserGroupPermissionSerializer
    renderer_classes = [UserRenderer]
    permission_classes = [IsAdminUser]
    authentication_classes = [SessionJWTAuthentication]