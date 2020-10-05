from django.urls import path, include
from . import views


app_name = 'accounts'

urlpatterns = [
  path('', views.user),
  path('<int:flag>/', views.set_flag),

  ## 이메일 인증
  path('<str:email>/', views.email),

  ## 지갑 생성, 조회
  path('wallet/<str:password>/', views.wallet_create),
  path('wallet/<int:id>/list/', views.wallet_read),

  ## 이력서 등록
  path('register/<int:id>/', views.register),

  ## 이력서 구매, 조회
  path('item/list/', views.item_read),
  path('item/<int:id>/', views.item_purchase),

]

