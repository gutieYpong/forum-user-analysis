from django.db.models import Prefetch
from rest_framework import viewsets, status, mixins
from rest_framework.response import Response

from .models import LihkgSon, Post, Comment
from .serializers import *

# from features.user.mixins import EmailPermissionMixin


class LihkgSonListRetrieveViewSet(mixins.RetrieveModelMixin,mixins.ListModelMixin,viewsets.GenericViewSet):
    queryset = LihkgSon.objects.all()
    serializer_class = LihkgSonSerializer
    lookup_field = 'pk'

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return LihkgSonDetailSerializer
        return LihkgSonSerializer


class PostListRetrieveViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Post.objects.all()
    lookup_field = 'pk'

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PostDetailSerializer
        return PostSerializer


class CommentListRetrieveViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    # queryset = Comment.objects.all().order_by('-created')
    queryset = Comment.objects.all()
    lookup_field = 'pk'

    # queryset = Comment.objects.prefetch_related(Prefetch('song_set', queryset=Song.objects.order_by('-timestamp')))

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CommentDetailSerializer
        return CommentSerializer