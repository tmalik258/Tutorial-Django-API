from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from snippets.views import snippet_detail, snippet_list


urlpatterns = [
	path('', snippet_list, name='snippet_list'),
	path('<int:pk>/', snippet_detail, name='snippet_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)