from django.contrib import admin
from .models import Profile, productTable
# Register your models here.

# superusers 
# iyanu_ad
# iyanu123



# admin.site.register(Profile)
admin.site.register(productTable)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user_id','position','state']
    
    