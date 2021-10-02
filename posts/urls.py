from django.urls import path
from django.views.decorators.cache import cache_page

from . import views


urlpatterns = [
	path('', views.AllPostsView.as_view(), name='all_posts'),
	path(
		'<uuid:pk>/',
		cache_page(60*15)(views.ConcretePostView.as_view()),
		name='concrete_post'),
]
