from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^auth/register/', views.RegistrationAPIView.as_view()),
    url(r'^sign_in/', views.SignInFormView.as_view()),
    url(r'^sign_up/', views.SignUpFormView.as_view()),
]