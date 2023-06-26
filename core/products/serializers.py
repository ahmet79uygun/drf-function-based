from rest_framework import serializers
from oscar.apps.catalogue.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

