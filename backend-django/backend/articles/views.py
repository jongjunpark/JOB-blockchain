from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Article
from .serializers import ArticleListSerializer, ArticleSerializer

# article_list
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def index(request):
    articles = Article.objects.all()
    serializer = ArticleListSerializer(articles, many=True)
    return Response(serializer.data)

# article_detail
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = ArticleSerializer(article)
    return Response(serializer.data)

# article_create
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create(request):
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
    return Response(serializer.data)

# article_delete
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    article.delete()
    return Response({'message': '성공적으로 삭제'})

# article_update
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = ArticleSerializer(data=request.data, instance=article)

    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response({'message': '성공적으로 수정'})
