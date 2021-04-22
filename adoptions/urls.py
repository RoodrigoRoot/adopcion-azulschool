from django.urls import path
from .views import AdoptionListCreateAPIView

urlpatterns = [
    path("adoptions/",AdoptionListCreateAPIView.as_view()),
]
