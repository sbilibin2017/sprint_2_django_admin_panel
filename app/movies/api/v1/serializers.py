
from django_filters import rest_framework as filters
from movies.models import Filmwork
from rest_framework import serializers


class StringListField(serializers.ListField):
    child = serializers.CharField()


class MoviesListSerializer(serializers.ModelSerializer):
    
    genres = StringListField()  
    actors = StringListField()
    directors = StringListField()
    writers = StringListField()

    class Meta:
        model = Filmwork
        fields = [
            'id', 'title', 'description', 'creation_date', 'rating', 'type',
            'genres', 'actors', 'directors', 'writers'

        ]