from rest_framework import serializers
from .models import Music

class MusicSerializer(serializers.ModelSerializer):

    class Meta:

        model = Music # Aqui passamos o modelo Music
        fields = '__all__' # Aqui passamos os campos title e seconds
        # Podendo ser assim também -> fields = ('title', 'seconds')