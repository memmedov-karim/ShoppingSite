from django.contrib import admin

from home.models import Settings,ContactFormMessage,UserProfileInfo
from django.contrib import admin


class ContactFormMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email','subject','message','status']
    list_filter = ['status']
class UserProfileInfoAdmin(admin.ModelAdmin):
    list_display = ['user_name','image_tag']


# Register your models here.
admin.site.register(Settings)
admin.site.register(ContactFormMessage,ContactFormMessageAdmin)
admin.site.register(UserProfileInfo,UserProfileInfoAdmin)
