from django.contrib.auth import get_user_model

from rest_framework import generics, permissions

from snippets.models import Snippet
from snippets.permissions import IsOwnerOrReadOnly
from snippets.serializers import SnippetSerializer, UserSerializer


class SnippetList(generics.ListCreateAPIView):
	"""
	List all code snippets, or create a new snippet
	"""
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
	"""
	Retrieve, update or delete a code snippet
	"""
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class UserList(generics.ListAPIView):
	"""
	List all users
	"""
	queryset = get_user_model().objects.all()
	serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
	"""
	Retrieve user
	"""
	queryset = get_user_model().objects.all()
	serializer_class = UserSerializer