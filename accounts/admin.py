
# users/admin.py
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

User = get_user_model()
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User, Address


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    readonly_fields=('date_joined', 'last_login', 'is_admin', 'is_active', 'is_staff', 'is_superuser')
    model = User
    list_display = ('first_name','last_name', 'email', 'username',)
    list_filter = ()  # Leave below fields empty
    search_fields = ()
    ordering = ()
    filter_horizontal = ()
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'address', 'image')}),
        (('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser'),
        }),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'image'),
        }),
    )
admin.site.register(User, CustomUserAdmin)

class AddressAdmin(admin.ModelAdmin):
    model = Address
    list_display = ('id','addressLine1', 'suburbCity', 'country',)

admin.site.register(Address, AddressAdmin)
