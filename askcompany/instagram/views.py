#instagram/views.py
import re
from django.contrib.auth import login
from django.core.checks import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpRequest, Http404
from django.views.generic.base import TemplateView
from django.views.generic.dates import YearArchiveView
from django.views.generic import ListView, DetailView, ArchiveIndexView, CreateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import UpdateView
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy

# @login_required
# def post_new(request) : 
#     if request.method == "POST" : 
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid() :
#             post = form.save(commit=False)
#             post.author=request.user # 현재 로그인 User의 Instance
#             post.save()
#             messages.success(request, '포스팅을 저장했습니다.')
#             return redirect(post)
#     else : 
#         form = PostForm()
    
#     return render(request, 'instagram/post_form.html',{
#         'form' : form,
#         'post' : None,
#     })

class PostCreateView(LoginRequiredMixin, CreateView) : 
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        messages.success(self.request,"포스팅을 저장했습니다.")
        return super().form_valid(form)

post_new = PostCreateView.as_view()

# @login_required
# def post_edit(request, pk) : 
#     post = get_object_or_404(Post, pk=pk)
    
#     #작성자 확인
#     if post.author != request.user : 
#         messages.error(request, "작성자만 수정할 수 있습니다.")
#         return redirect(post)

#     if request.method == "POST" : 
#         form = PostForm(request.POST, request.FILES, instance=post)
#         if form.is_valid() :
#             post = form.save()
#             messages.success(request, '포스팅을 수정했습니다.')
#             return redirect(post)
#     else : 
#         form = PostForm(instance=post)
    
#     return render(request, 'instagram/post_form.html',{
#         'form' : form,
#         'post' : post,
#     })

class PostUpdateView(LoginRequiredMixin, UpdateView) : 
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        messages.success(self.request,"포스팅을 수정했습니다.")
        return super().form_valid(form)

post_edit = PostUpdateView.as_view()

# @login_required
# def post_delete(request,pk):
#     post=get_object_or_404(Post,pk=pk)
#     if request.method == 'POST' : 
#         post.delete()
#         messages.success(request,'포스트를 삭제했습니다.')
#         return redirect('instagram:post_list')
#     return render(request,'instagram/post_confirm_delete.html',{
#         'post':post,
#     })

class PostDeleteView(LoginRequiredMixin, DeleteView) :
    model = Post
    success_url = reverse_lazy('instagram:post_list')
    # def get_success_url(self) :
    #     return reverse('instagram:post_list')

post_delete = PostDeleteView.as_view()

post_list = login_required(ListView.as_view(model=Post, paginate_by=3))

@method_decorator(login_required, name='dispatch')
class PostListView(ListView) : 
    model = Post
    paginate_by = 3

post_list = PostListView.as_view()

# @login_required
# def post_list(request) : #호출 당시에 모든 인자를 전달 받음
#      qs = Post.objects.all() #사용할 쿼리문을 만들 준비
#      q = request.GET.get('q', '') # q라는 인자가 있으면 받아오고 없다면 빈문자열을 받음
#      if q : 
#          qs = qs.filter(message__icontains=q) # q가 존재한다면 쿼리문 생성
    
#      messages.info(request, 'messages 테스트')

#      return render(request,'instagram/post_list.html',{ #instagram/templates/instagram/post_list.html
#          'post_list' : qs,
#          'q':q,
#      }) # render를 통해 손쉽게 html문자열을 조합

#def post_detail(request, pk) : 
    #post = get_object_or_404(Post, pk=pk)
    #try : 
    #    post = Post.objects.get(pk=pk)
    #except Post.DoesNotExist : 
    #    raise Http404
    #return render(request,'instagram/post_detail.html',{
    #    'post':post,
    #})
#post_detail = DetailView.as_view(model=Post)

class PostDetailView(DetailView)  :
    model = Post
    def get_queryset(self) :
        qs = super().get_queryset() # DetailView의 get_queryser() 함수
        if not self.request.user.is_authenticated: # 만약 로그인되지 않은 사용자라면 
            qs = qs.filter(is_public = True) #qs를 is_ppublic = True로 필터링
        return qs

post_detail = PostDetailView.as_view()

# def archives_year(request,year) : 
#     return HttpResponse(f"{year}년 archives")

post_archive = ArchiveIndexView.as_view(model=Post, date_field='created_at', paginate_by = 3)

post_archive_year = YearArchiveView.as_view(model=Post, date_field='created_at', make_object_list = True)
