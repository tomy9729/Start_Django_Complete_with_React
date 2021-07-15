#instagram/admin.py
from django.contrib import admin
from .models import Post, Comment, Tag
from django.utils.safestring import mark_safe

@admin.register(Post) 
class PostAdmin(admin.ModelAdmin) : 
    list_display = ['pk','message','photo_tag','message_length','created_at','is_public','updated_at'] #primary key(id)
    list_display_links = ['message'] # 여러개 넣을 수 있다.
    list_filter = ['created_at', 'is_public']
    search_fields = ['message'] # 메세지를 통해 검색

    def photo_tag(self, post) : 
        if post.photo : 
            return mark_safe(f'<img src = "{post.photo.url}" style="width:50px"/>')
        return None
    def message_length(self, post):
        return f"{len(post.message)}글자"

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin) : 
    pass

@admin.register(Tag) 
class TagAdmin(admin.ModelAdmin):
    pass