from django.contrib import admin
from . models import UserProfile

# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'default_phone_number',
        'default_country',
        'profile_image',
    )

    ordering = ('user',)


admin.site.register(UserProfile, UserProfileAdmin)
