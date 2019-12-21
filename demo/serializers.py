from rest_framework import serializers
from .models import Book, BookNumber, Character, Author


class BookNumberSerializzer(serializers.ModelSerializer):
    class Meta:
        model = BookNumber
        fields = ['isbn_10', 'isbn_13', 'id']


class CharacterSerializzer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ['id', 'name']


class AuthorSerializzer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'surname']


class BookSerializer(serializers.ModelSerializer):
    number = BookNumberSerializzer(many=False)
    characters = CharacterSerializzer(many=True)
    authors = AuthorSerializzer(many=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'description', 'price', 'number', 'characters', 'authors']


class BookMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title']