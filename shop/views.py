import csv

from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from shop.filters import ClientFilter
from shop.models import Client
from shop.serializers import ClientSerializer
from shop.services import import_clients_from_csv


class ClientViewSet(GenericViewSet, ListModelMixin):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ClientFilter

    @action(detail=False, methods=["get"])
    def import_data_to_db(self, request):
        if Client.objects.exists():
            raise ValidationError("Client data already imported")
        import_clients_from_csv()
        return Response({"success": "Data imported successfully"}, status=status.HTTP_200_OK)

    @action(detail=False, methods=["get"])
    def export_csv(self, request):
        clients = self.filter_queryset(self.get_queryset())
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="clients.csv"'

        writer = csv.writer(response)
        writer.writerow(
            ['Category', 'First Name', 'Last Name', 'Email', 'Gender', 'Birth Date']
        )

        for client in clients:
            writer.writerow([
                client.category,
                client.first_name,
                client.last_name,
                client.email,
                client.gender,
                client.birth_ate,
            ])

        return response
