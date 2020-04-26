from django.contrib import admin
from core.models import Post, Event, CommentPost


admin.site.register(Post)
admin.site.register(Event)
admin.site.register(CommentPost)
