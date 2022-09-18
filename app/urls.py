from django.urls import path

from .views import home, generate_excel

urlpatterns = [
    path("", home, name="home"),
    path("excel/", generate_excel, name="excel"),
]
