from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from accounts.models import Account
from accounts.serializers import AccountSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class AccountViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = AccountSerializer
    queryset = Account.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

