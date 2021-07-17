from django.contrib.auth.views import LoginView,LogoutView
from django.urls import path
from . import views
from .forms import LoginFrom

urlpatterns = [
    path('login/',LoginView.as_view(template_name="accounts/login_form.html", form_class = LoginFrom), name='login'),
    path('logout/', LogoutView.as_view(),name="logout"),
    path('profile/', views.profile, name = "profile"),
    path('profile/edit/', views.profile_edit, name = "profile_edit"),
    path('signup/', views.signup, name = "signup"),
]