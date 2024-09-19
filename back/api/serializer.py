from rest_framework import serializers
from .models import Filmes, Genero, Classificacao


class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = ["id", "genre"]

class ClassificacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classificacao
        fields = ["id", "classificacao"]

class FilmesSerializer(serializers.ModelSerializer):
    # genre = GeneroSerializer()
    class Meta:
        model = Filmes
        fields = ['id', 'titulo', 'genre', 'ano', 'idioma', 'classif', ]
        # "urlImage", "imagem"
