from django.urls import path
from . import views

app_name = 'books'
urlpatterns = [
    path('books/', views.book_list, name='book_list'),    
    path('books/<int:book_pk>/', views.book_detail),
    path('books/<int:book_pk>/comments/', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail),
]
