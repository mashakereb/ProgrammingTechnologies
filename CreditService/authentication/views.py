from logging import Logger

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.pagination import PageNumberPagination

from django.views.generic import TemplateView

from .serializers import ProfileSerializer, UserSerializer
from .models import Profile

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
            return Response(serializer.data, status=201)
        logger.info('Data is not valid')
        return Response(serializer.errors, status=400)


class ProfileAPIView(APIView):
    """
    CRUD for single customer
    """
    def get(self, request, id, **kwargs):
        """
        Get customer by id
        :param request:
        :param id:
        :param format:
        :return:
        """
        try:
            item = Profile.objects.get(pk=id)
            serializer = ProfileSerializer(item)
            return Response(serializer.data)
        except Profile.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        """
        Update customer by id
        :param request:
        :param id:
        :param format:
        :return:
        """
        try:
            item = Profile.objects.get(pk=id)
        except Profile.DoesNotExist:
            return Response(status=404)
        serializer = ProfileSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        """
        Delete customer by id
        :param request:
        :param id:
        :param format:
        :return:
        """
        try:
            item = Profile.objects.get(pk=id)
        except Profile.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class ProfileAPIListView(APIView):

    def get(self, request, **kwargs):
        """
        Get Customer list
        :param request:
        :param format:
        :return:
        """
        items = Profile.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = ProfileSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, **kwargs):
        """
        Create new Customer
        :param request:
        :param format:
        :return:
        """
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class SignInFormView(TemplateView):
    """
    Render sign in form
    """
    template_name = 'sign_in_form.html'


class SignUpFormView(TemplateView):
    """
    Render sign up form
    """
    template_name = 'sign_up_form.html'
