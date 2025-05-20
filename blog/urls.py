from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    # 다른 URL 패턴도 추가 가능
]
