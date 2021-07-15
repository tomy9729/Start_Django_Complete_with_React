from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

# @login_required
# def profile(request) : 
#     return render(request,'accounts/profile.html')

class ProfileView(LoginRequiredMixin, TemplateView) : 
    template_name = 'accounts/profile.html'

profile = ProfileView.as_view()

from django.views.generic import UpdateView
from accounts.forms import ProfileForm

# class ProfileUpdateView(LoginRequiredMixin,UpdateView):
#     model = Profile
#     form_class = ProfileForm

# profile_edit = ProfileUpdateView.as_view()

from accounts.models import Profile

@login_required
def profile_edit(request):
    try: 
        profile = request.user.profile #프로필이 존재한다면 사용자의 프로필을 받고
    except Profile.DoesNotExist : 
        profile = None # 존재하지 않는다면 None으로 설정

    if request.method == "POST" : #POST일 경우
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid() : 
            profile = form.save(commit=False)
            profile.user = request.user #user 지정
            profile.save()
            return redirect("profile")
    else : 
        form = ProfileForm(instance=profile)
    return render(request, "accounts/profile_form.html",{
        "form":form,
    })

def signup(request) : 
    pass

def logout(request):
    pass