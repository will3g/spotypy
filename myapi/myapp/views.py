from rest_framework import generics
from .models import Music
from django.shortcuts import render
from .serializers import MusicSerializer

class MusicList(generics.ListCreateAPIView):

    queryset = Music.objects.all()
    serializer_class = MusicSerializer
