from uuid import uuid4

from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


User = get_user_model()


class Post(models.Model):
	uuid = models.UUIDField(primary_key=True, editable=False, default=uuid4)
	title = models.CharField(max_length=100, unique=True)
	short_description = models.CharField(max_length=255)
	description = models.TextField()
	pub_date = models.DateField(auto_now_add=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	class Meta:
		db_table = 'posts'
		ordering = ('-pub_date', 'title')

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('concrete_post', args=(str(self.pk),))
