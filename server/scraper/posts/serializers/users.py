from rest_framework import serializers

from posts.models import LihkgSon
from .posts import PostSerializer
from .comment import CommentSerializer


class LihkgSonSerializer(serializers.ModelSerializer):
    user_url = serializers.HyperlinkedIdentityField(view_name='users-detail', lookup_field='pk')
    user_posts = PostSerializer(many=True, read_only=True)
    user_comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = LihkgSon
        fields = [
            'lihkgson_id',
            'user_url',
            'nickname',
            'user_posts',
            'user_comments',
        ]


class LihkgSonDetailSerializer(LihkgSonSerializer):

    class Meta(LihkgSonSerializer.Meta):
        fields = [
            'lihkgson_id',
            'nickname',
            'user_posts',
            'user_comments',
        ]