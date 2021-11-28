from django.shortcuts import render
from .models import *
from rest_framework.response import Response
from rest_framework import generics, status
from .serializers import *
from django.shortcuts import render, get_object_or_404
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class SnippetListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TextSnippetSerializer

    def list(self, request, *args, **kwargs):
        serializer_context = {
            'request': request,
        }
        queryset = TextSnippet.objects.select_related('tag').all()
        if queryset:
            serializer = self.get_serializer(queryset, many=True, context=serializer_context)
            return Response({"count":queryset.count(),"snippets":serializer.data,'message':"Success"})
        else:
            return Response({"count":0,"snippets":[],"message":"No Data"})


class SnippetDetailView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = TextSnippet.objects.all()
    serializer_class = TextSnippetSerializer
    lookup_fields = ['id']
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if not instance:
            return Response({"snippet":[],"message":"No Data"})
        else:
            serializer = self.get_serializer(instance)
            return Response({"snippet":serializer.data,'message':"Success"})


class CreateTextSnippetView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = SnippetCreateSerializer
    model = TextSnippet

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=self.request.data)
        if serializer.is_valid():
            snippet_obj = serializer.create(validated_data=serializer.validated_data)
            snippet_obj.save()
            if snippet_obj:
                return Response({"status": True, "message": "Success"})
            else:
                Response({"status": True, "message": serializer.errors})
        return Response({"status": True, "message": serializer.errors})


class UpdateTextSnippetView(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangeTextSnippetSerializer
    model = TextSnippet

    def get_object(self):
        try:
            obj = self.model.objects.get(pk=self.kwargs.get('pk'))
        except:
            obj = None
        return obj

    def update(self, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(data=self.request.data)
        if serializer.is_valid():
            offer_obj = serializer.update(serializer.validated_data, instance)
            if offer_obj:
                return Response({"status": True, "message": "Success!"})
            else:
                return Response({"status": False, "message": "No Data"})

        return Response({"status": False, "message": serializer.errors})


class TagListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TagSerializer

    def list(self, request, *args, **kwargs):
        serializer_context = {
            'request': request,
        }
        queryset = Tag.objects.all()
        if queryset:
            serializer = self.get_serializer(queryset, many=True, context=serializer_context)
            return Response({"count":queryset.count(),"tags":serializer.data,'message':"Success"})
        else:
            return Response({"count":0,"tags":[],"message":"No Data"})


class TagDetailView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_fields = ['id']
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if not instance:
            return Response({"tag":[],"message":"No Data"})
        else:
            serializer = self.get_serializer(instance)
            return Response({"tag":serializer.data,'message':"Success"})


class CreateTagView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TagCreateSerializer
    model = Tag

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=self.request.data)
        if serializer.is_valid():
            tag_obj = serializer.create(validated_data=serializer.validated_data)
            tag_obj.save()
            if tag_obj:
                return Response({"status": True, "message": "Success"})
            else:
                Response({"status": True, "message": serializer.errors})
        return Response({"status": True, "message": serializer.errors})


def deleteMutiple(self, request, pk):
    pk_ids = request.query_params.get('pk_ids', None)
    if pk_ids:
        for i in pk_ids.split(','):
            get_object_or_404(TextSnippet, pk=int(i)).delete()
    else:
        get_object_or_404(TextSnippet, pk=pk).delete()
    return Response({"status": True, "message": "Deleted!"})