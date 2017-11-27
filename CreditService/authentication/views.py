from logging import Logger

from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from django.views.generic import TemplateView

from django.shortcuts import redirect, render
from .serializers import UserSerializer

from . import errors

logger = Logger('auth views')


class RegistrationAPIView(APIView):
    """
    Handle user registration
    """
    permission_classes = (AllowAny,)

    def post(self, request, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('/login')

        logger.info('Auth data is not valid')
        return render(request, 'registration/signup.html',
                      {'form': {
                          'data': serializer.data,
                          'errors': [errors.INCORRECT_CREDENTIALS]
                      }})

    def get(self, request):
        return render(request, 'registration/signup.html')


class SignUpFormView(TemplateView):
    """
    Render sign up form
    """
    template_name = 'registration/signup.html'


class HomeView(TemplateView):
    """
    Render sign up form
    """
    template_name = 'index.html'
