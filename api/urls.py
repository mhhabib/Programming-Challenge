from django.urls import path
from .views import ApiView

urlpatterns = [
    path('api/', ApiView.as_view(), name="api"),
]