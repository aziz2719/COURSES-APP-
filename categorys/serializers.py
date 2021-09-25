from rest_framework import serializers
from .models import Category, Branch, Contact

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ('__all__')


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('__all__')


class CategorySerializer(serializers.ModelSerializer):
    categor1 = BranchSerializer(many=True, read_only=True)
    categor2 = ContactSerializer(read_only=True, many=True)
    class Meta:
        model = Category
        fields = ('id', 'name', 'image', 'categor1', 'categor2')
