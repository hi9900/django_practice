from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/detail/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/comments/', views.create_comments, name='create_comments'),
    path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.delete_comments, name='delete_comments'),
    path('<int:article_pk>/likes/', views.likes, name='likes'),
]
