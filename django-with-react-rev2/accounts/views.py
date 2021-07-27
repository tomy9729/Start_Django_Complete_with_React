from accounts.forms import SingupForm
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import SingupForm

def signup(request):
    if request.method == 'POST' : 
        form = SingupForm(request.POST)
        if form.is_valid():
            signed_user = form.save()
            messages.success(request,"회원가입을 환영합니다.")
            signed_user.send_welcome_email() #현재는 속도가 좀 느리기 때문에 추후에 Celery로 처리하는 것을 추천
            next_url = request.GET.get('next','root')
            return redirect(next_url)
    else : 
        form = SingupForm()
    return render(request, 'accounts/signup_form.html',{
        'form' : form,
    })
    