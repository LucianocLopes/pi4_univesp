from django.urls import path
from .views import RegistroUsuarioView, ProfileUpdateView, profile_detail_view

urlpatterns = [
    path('registro/', RegistroUsuarioView.as_view(), name='registro'),
    # URL for the profile update view
    path('profile/edit/<int:pk>', ProfileUpdateView.as_view(), name='profile_edit'),
    # URL for the user's profile detail page. The `username` is a URL parameter.
    path('profile/<int:pk>/', profile_detail_view, name='profile_detail'),
]