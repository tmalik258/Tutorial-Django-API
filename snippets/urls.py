from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from snippets.views import SnippetDetail, SnippetList, UserDetail, UserList


urlpatterns = [
	path('users/', UserList.as_view(), name='user_list'),
	path('users/<int:pk>/', UserDetail.as_view(), name='user_list'),
	path('', SnippetList.as_view(), name='snippet_list'),
	path('<int:pk>/', SnippetDetail.as_view(), name='snippet_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)