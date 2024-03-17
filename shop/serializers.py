from rest_framework import serializers

from shop.models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = (
            "id",
            "category",
            "first_name",
            "last_name",
            "email",
            "gender",
            "birth_ate",
        )
