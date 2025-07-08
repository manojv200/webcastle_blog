from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from blog.models import Comments, TblUser

# Register your models here.
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = TblUser
        fields = ('username', 'email', 'mobile')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = TblUser
        fields = ('username', 'email', 'mobile')

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = TblUser

    list_display = ('username', 'email', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('mobile',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('mobile',)}),
    )

admin.site.register(TblUser, CustomUserAdmin)