from rest_framework import serializers

from posts.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    nickname = serializers.ReadOnlyField(source='author.nickname')
    comment_url = serializers.HyperlinkedIdentityField(view_name='comments-detail', lookup_field='pk')

    class Meta:
        model = Comment
        fields = [
            'comment_url',
            'nickname',
            'created',
        ]


class CommentDetailSerializer(CommentSerializer):
    class Meta(CommentSerializer.Meta):
        fields = [
            'post',
            'comment_id',
            'author',
            'content',
            'created',
        ]
