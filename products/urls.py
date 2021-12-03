from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('create/', views.create, name='create'),
    path('<int:product_id>/', views.detail, name='detail'),
    path('upvote/<int:product_id>/', views.upvote, name='upvote'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)