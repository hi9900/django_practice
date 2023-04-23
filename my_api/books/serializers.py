from rest_framework import serializers
from .models import Book, Comment

# Q 1.
class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'content', 'created_at', 'updated_at')


class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('book', )

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep.pop('book', None)
        return rep


class BookSerializer(BookListSerializer):
    comment_cnt = serializers.IntegerField(source='comment_set.count', read_only=True)
    # comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comment_set = CommentListSerializer(many=True, read_only=True)
    class Meta(BookListSerializer.Meta):
        # model = Book
        fields = BookListSerializer.Meta.fields + ('comment_set', 'comment_cnt', )

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['comments'] = rep.pop('comment_set', [])
        return rep