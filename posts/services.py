from django.shortcuts import get_object_or_404

from .models import Post


def get_all_posts():
	all_posts = Post.objects.all()
	return all_posts


def get_concrete_post(pk):
	concrete_post = get_object_or_404(Post, pk=pk)
	return concrete_post
