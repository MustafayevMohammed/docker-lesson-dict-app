from django.urls import path
from dictionary import views

app_name = "dictionary"

urlpatterns = [
    path("",views.HomePageView.as_view(),name="home"),
    path("detail/",views.DetailPageView.as_view(),name="detail"),
]