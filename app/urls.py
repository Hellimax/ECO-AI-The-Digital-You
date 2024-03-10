from django.urls import path
from .views import homepage, get_interests, generate_tweet

urlpatterns = [
    path('', homepage, name='homepage'),
    path('interests/', get_interests, name='get_interests'),
    path('generate/', generate_tweet, name='generate_tweet')
]
