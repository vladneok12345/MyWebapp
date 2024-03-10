from django.contrib import admin
from .models import Post, PostPoint, Comment, Trip
# Register your models here.

admin.site.register(Post)
admin.site.register(PostPoint)
admin.site.register(Trip)
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("name","email","post","created","active")
    list_filter = ("active","created","updated")
    search_fields = ("name","email", "post", "body")