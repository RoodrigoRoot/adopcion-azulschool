from django.urls import path
from .views import PetsListCreateAPIView

urlpatterns = [
    path("pets/", PetsListCreateAPIView.as_view()),
]
