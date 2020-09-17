from rest_framework import serializers
from .models import Article
# from .models import Image
from accounts.serializers import UserSerializer

class ArticleListSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Article
        fields = ('id', 'user')

class ArticleSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    image = serializers.ImageField(use_url=True)
    class Meta:
        model = Article
        fields = '__all__'

# class ImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Image
#         fields = '__all__'