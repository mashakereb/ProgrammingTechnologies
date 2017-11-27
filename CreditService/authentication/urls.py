from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^signup/', views.RegistrationAPIView.as_view()),
    url(r'^$', views.HomeView.as_view()),
]