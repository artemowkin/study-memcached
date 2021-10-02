from django.shortcuts import render
from django.views import View

from .services import get_all_posts, get_concrete_post


class AllPostsView(View):

	def get(self, request):
		all_posts = get_all_posts()
		return render(request, 'posts/all_posts.html', {'posts': all_posts})


class ConcretePostView(View):

	def get(self, request, pk):
		requested_post = get_concrete_post(pk)
		return render(
			request, 'posts/concrete_post.html', {'post': requested_post}
		)
