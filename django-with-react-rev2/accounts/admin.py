from django.contrib import admin
from. models import User

@admin .register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username','email','website_url','is_active','is_superuser']
    pass

# Register your models here.
