from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'short_description', 'author', 'pub_date')
	search_fields = ('title', 'short_description')
	raw_id_fields = ('author',)
