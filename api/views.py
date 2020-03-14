from rest_framework import viewsets, permissions
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from webapp.models import File
from rest_framework.viewsets import ModelViewSet
from api.serializers import FileSerializer
from rest_framework.permissions import DjangoModelPermissions, AllowAny, DjangoModelPermissionsOrAnonReadOnly, \
    IsAuthenticated, BasePermission


class FileViewSet(viewsets.ModelViewSet):
    # authentication_classes = SessionAuthentication
    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = File.objects.all()
    serializer_class = FileSerializer
