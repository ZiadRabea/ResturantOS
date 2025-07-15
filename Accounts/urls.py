from django.urls import path
from.views import sign_up, profile
urlpatterns = [
    path('sign_up/', sign_up),
    path('profile/<int:id>/', profile),
    ]