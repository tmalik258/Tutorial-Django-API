from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from snippets.views import SnippetDetail, SnippetList


urlpatterns = [
	path('', SnippetList.as_view(), name='snippet_list'),
	path('<int:pk>/', SnippetDetail.as_view(), name='snippet_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)