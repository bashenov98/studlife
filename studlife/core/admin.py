from django.contrib import admin

# Register your models here.
from core.models import Post, Event, CommentPost


admin.site.register(Post)
admin.site.register(Event)
admin.site.register(CommentPost)
