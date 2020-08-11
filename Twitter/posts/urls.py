from django.urls import path, include

from .views import AddPostView


app_name = 'posts'
urlpatterns = [
    path('add_post/', AddPostView.as_view(), name='add-post')
]
