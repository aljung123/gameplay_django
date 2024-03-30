from django.urls import path, include
from .views import main, delete_comment
urlpatterns = [
    path('', main, name = 'home'),
    path('delete_comment/<int:comment_id>', delete_comment, name="delete_comment")
]