from django.urls import path

from auth_ex import views as user_views

app_name = 'auth_ex'
urlpatterns = [
    path('register/', user_views.UserCreateView.as_view(), name='register'),
]
