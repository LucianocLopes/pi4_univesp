from django.urls import path
from core import views

app_name = 'core'

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("about/", views.AboutUsView.as_view(), name="about_us"),
]
