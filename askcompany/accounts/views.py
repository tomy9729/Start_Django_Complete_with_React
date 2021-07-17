from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

# @login_required
# def profile(request) : 
#     return render(request,'accounts/profile.html')

class ProfileView(LoginRequiredMixin, TemplateView) : 
    template_name = 'accounts/profile.html'

profile = ProfileView.as_view()

from django.views.generic import UpdateView

from accounts.forms import ProfileForm
from accounts.models import Profile

# class ProfileUpdateView(LoginRequiredMixin,UpdateView):
#     model = Profile
#     form_class = ProfileForm

# profile_edit = ProfileUpdateView.as_view()


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

from django.contrib.auth import get_user_model, login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings

User = get_user_model()

class SignupView(CreateView) : 
    model = User
    form_class = UserCreationForm
    success_url = settings.LOGIN_REDIRECT_URL
    template_name = "accounts/signup_form.html"

    def form_valid(self, form):
        respone = super().form_valid(form)
        user = self.object
        auth_login(self.request, user)
        return respone

signup = SignupView.as_view()

