from django.shortcuts import render
from .models import Post

def post_list(request) : 
    qs = Post.objects.all() #QuerySet  데이터베이스에 있는 모든  post를 가져옴
    return render(request, 'blog1/post_list.html',{
        'post_list' : qs, #가져온 post 목록을 넘겨준
    })
