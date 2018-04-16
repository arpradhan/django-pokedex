from rest_framework import serializers

from .models import Pokemon


class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ('id', 'identifier', 'species_id', 'height',
                  'weight', 'base_experience', 'order', 'is_default',)
