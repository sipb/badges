from django.urls import path

from .views import home, badges

urlpatterns = [
    path('home/', home, name='home'),
    path('badges/', badges, name='badges')
]