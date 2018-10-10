# coding: utf-8

# Also referenced:
# https://www.django-rest-framework.org/api-guide/relations/#writable-nested-serializers

# frozenset??
from rest_framework import serializers
from .models import User, Entry


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'mail')


class EntrySerializer(serializers.ModelSerializer):
    # overwrite the serializer of author
    author = UserSerializer()

    class Meta:
        model = Entry
        fields = ('title', 'body', 'created_at', 'status', 'author')

    # To be fixed...:
    # IntegrityError at /api/entries/
    #    NOT NULL constraint failed: blog_entry.author_id

    # def create(self, validated_data):
    #     authors_data = validated_data.pop('author')
    #     entry = Entry.objects.create(**validated_data)
    #     for author_data in authors_data:
    #         User.objects.create(entry=entry, **author_data)
    #     return entry
