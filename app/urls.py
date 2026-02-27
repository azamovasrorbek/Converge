from django.urls import path
from .views import home, post_comment
urlpatterns = [
    path('', home, name='home'),
    path('post-comment/', post_comment, name='post_comment')
]