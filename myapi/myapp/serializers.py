from rest_framework import serializers
from .models import Music, Album, Band, Member

# A classe RetrieveUpdateDestroyAPIView implementa os métodos GET, PUT, PATCH e DELETE

class MusicSerializer(serializers.ModelSerializer):

    class Meta:

        model = Music # Aqui passamos o modelo Music
        fields = '__all__' # Aqui passamos os campos title e seconds
        # Podendo ser assim também -> fields = ('title', 'seconds')

class AlbumSerializer(serializers.ModelSerializer):

    class Meta:

        model = Album
        fields = '__all__'

class BandSerializer(serializers.ModelSerializer):

    class Meta:

        model = Band
        fields = '__all__'

class MemberSerializer(serializers.ModelSerializer):

    class Meta:

        model = Member
        fields = '__all__'