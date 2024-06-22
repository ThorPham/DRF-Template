from django.urls import path, include
from app.apis import SupporterAV
urlpatterns = [
    path('supporter/', SupporterAV.as_view(), name='supporter'),
]