from django.db import models
from django.conf import settings
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.
class Article(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True
    )
    phone_number = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    # highschool = models.CharField(max_length=100)
    # university = models.CharField(max_length=100)
    # university_grade = models.FloatField()
    # university_status = models.CharField(max_length=50)
    # master_degree = models.CharField(max_length=100)
    # doctor_degree = models.CharField(max_length=100)
    image = models.ImageField(upload_to="media")
    imgae_thumnail = ImageSpecField(source='image',
                        processors=[ResizeToFill(300,300)],
                        format='JPEG',
                        options={'quality' : 60}
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# 다중 이미지 업로드
# class Image(models.Model):
#     article = models.ForeignKey(Article, blank=True, null=True, on_delete=models.CASCADE)
#     image = ProcessedImageField(
#         upload_to = 'media', # 저장 위치
#         processors = [ResizeToFill(300, 300)],
#         format = 'JPEG',
#         options = {'quality': 60},
#         null = True
#     )