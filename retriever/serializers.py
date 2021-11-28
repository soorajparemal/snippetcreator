from rest_framework import serializers
from rest_framework.relations import HyperlinkedIdentityField
from .models import *

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ['id', 'title']

class TextSnippetSerializer(serializers.ModelSerializer):
    detail_url = HyperlinkedIdentityField(view_name='snippet_detail')

    class Meta:
        model = TextSnippet
        fields = ['id', 'title', 'timestamp','created_by', 'tag', 'detail_url']



class SnippetCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextSnippet
        fields = ['title', 'timestamp','created_by','tag']

        def create(self,validated_data):
            snippet = TextSnippet.objects.create(**validated_data)
            return snippet


class ChangeTextSnippetSerializer(serializers.ModelSerializer):

    class Meta:
        model = TextSnippet
        fields = ['title', 'timestamp','created_by','tag']

    def update(self, validated_data, instance):

        try:
            title = validated_data.get('title')
            timestamp = validated_data.get('timestamp')
            created_by = validated_data.get('created_by')
            tag = validated_data.get('tag')

            if title:
                instance.title = title

            if timestamp:
                instance.timestamp = timestamp

            if created_by:
                instance.created_by = created_by

            if tag:
                instance.tag = tag

            instance.save()
            return instance
        except:
            return False


class TagCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['title']

        def create(self,validated_data):
            tag = Tag.objects.create(**validated_data)
            return tag