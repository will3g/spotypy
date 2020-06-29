from rest_framework import generics
from .models import Music, Album, Band, Member
from .serializers import MusicSerializer, AlbumSerializer, BandSerializer, MemberSerializer
from django_filters import rest_framework as filters
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

# DjangoFilterBackend é o filtro padrão dessa view
# filter_fields indica quais campos podem ser passados como filtros

# MUSIC
class MusicList(generics.ListCreateAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = (IsAuthenticated, )
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'

class MusicDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = (IsAuthenticated, )
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'

# ALBUM
class AlbumList(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = (IsAuthenticated, )
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'

class AlbumDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = (IsAuthenticated, )
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'

# BAND
class BandList(generics.ListCreateAPIView):
    queryset = Band.objects.all()
    serializer_class = BandSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = (IsAuthenticated, )
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'

class BandDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Band.objects.all()
    serializer_class = BandSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = (IsAuthenticated, )
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'

# MEMBER
class MemberList(generics.ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = (IsAuthenticated, )
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'

class MemberDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = (IsAuthenticated, )
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'
