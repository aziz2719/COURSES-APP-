from django.shortcuts import render
from django.http import Http404

from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Category, Branch, Contact
from .serializers import CategorySerializer, BranchSerializer, ContactSerializer


class CategoryView(APIView):

    def get(self, request, format=None):
        categ = Category.objects.all()
        serializer = CategorySerializer(categ, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetail(APIView):

    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        categ = self.get_object(pk)
        serializer = CategorySerializer(categ)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        categ = self.get_object(pk)
        serializer = CategorySerializer(categ, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        categ = self.get_object(pk)
        categ.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BranchView(ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    lookup_field = 'pk'


class ContactView(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    lookup_field = 'pk'