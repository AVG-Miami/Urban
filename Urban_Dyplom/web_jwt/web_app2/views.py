from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, AllowAny, IsAuthenticated
from rest_framework import permissions
from .models import Students
from .serializers import StudentSerializer



# Create your views here.
class IsAdminOrReadOnly(permissions.BasePermission):
    """
    запись может удалять только администратор, а просматривать все пользователи
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    разрешим изменять запись только автору, то есть,
    пользователю, который ее добавил. А просматривать,
    по прежнему, всем пользователям.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions are only allowed to the owner of the snippet.
        return obj.user == request.user


class StudentsAPIView(generics.ListCreateAPIView):
    """
     добавлять записи могут только авторизованные пользователи
    """
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


#
class StudentsAPIUpdate(generics.RetrieveUpdateAPIView):
    """
    изменять запись может только автор,
    а просматривать, разрешено всем пользователям
    """
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (IsAuthenticated,)
    #permission_classes = (IsOwnerOrReadOnly,)


class StudentsAPIDestroy(generics.RetrieveDestroyAPIView):
    """
    удалять запись может только администратор,
    а просматривать, разрешено всем пользователям
    """
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (IsAdminOrReadOnly,)

