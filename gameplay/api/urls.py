from django.urls import path
from .views import home_view , delete_comment, register, login_view, logout_view
urlpatterns = [
    path('', home_view, name = 'home'),
    path('delete_comment/<int:comment_id>', delete_comment, name="delete_comment"),
    path('register', register, name="register"),
    path('login', login_view, name="login"),
    path('logout', logout_view, name="logout"),

]