from django.urls import path

from snippets.views import snippet_detail, snippet_list


urlpatterns = [
	path('', snippet_list, name='snippet_list'),
	path('<int:pk>/', snippet_detail, name='snippet_detail'),
]