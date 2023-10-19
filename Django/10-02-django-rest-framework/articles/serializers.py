from rest_framework import serializers
from .models import Article ,Comment


class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content',)

class CommentSerializer(serializers.ModelSerializer):
    class ArticleTitleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('title',)
    #override???
    article = ArticleTitleSerializer(read_only=True)
    # 새로운 id 만들 떄 article까지 작성할 필요 없어! read_only니까?????
    class Meta:
        model = Comment
        fields = '__all__'
        #read_only_fields = ('article',) #(읽기전용필드, 유효성검사에서 빠짐)


class ArticleSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    class Meta:
        model = Article
        fields = '__all__'


