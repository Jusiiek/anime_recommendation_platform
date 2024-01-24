from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.generics import get_object_or_404

from user.models import User
from user.serializers import UserSerializer

from utils import PaginatedListMixin


class UserViewSet(PaginatedListMixin, viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def list(self, request):
        user_qs = self.queryset
        if 'role' in request.GET.keys() and request.GET['role']:
            user_qs = user_qs.filter(user_role__user_role__name=request.GET['role'])

        return self.paginate(user_qs, request)

    def retrieve(self, request, pk=None, **kwargs):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = self.serializer_class(user)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        user_data = request.data

        new_user = self.serializer_class(validated_data=user_data)
        new_user.save()

        serializer = self.serializer_class(new_user)

        # todo add send email?

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None, **kwargs):
        user_object = self.get_object()
        user_data = request.data

        user_serializer = self.serializer_class(instance=user_object, data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()

        return Response(user_serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk=None, **kwargs):
        user_object = self.get_object()
        self.perform_destroy(user_object)
        return Response(status=status.HTTP_204_NO_CONTENT)
