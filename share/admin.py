from django.contrib import admin

# Register your models here.
from share.models import Post, Comment, PostImage, Category

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(PostImage)
admin.site.register(Category)

