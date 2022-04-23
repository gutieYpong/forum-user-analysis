from rest_framework import serializers

from posts.models import Post
from .comment import CommentSerializer


class PostSerializer(serializers.ModelSerializer):
    nickname = serializers.ReadOnlyField(source='author.nickname')
    post_url = serializers.HyperlinkedIdentityField(view_name='posts-detail', lookup_field='pk')

    class Meta:
        model = Post
        fields = [
            'created',
            'post_url',
            'nickname',
            'topic',
        ]


class PostDetailSerializer(PostSerializer):
    post_comments = CommentSerializer(many=True, read_only=True)

    class Meta(PostSerializer.Meta):
        fields = [
            'created',
            'post_id',
            'author',
            'nickname',
            'topic',
            'post_comments'
        ]