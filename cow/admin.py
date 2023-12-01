from django.contrib import admin
from .models import cow_info_model
# Register your models here.



class cow_info_admin(admin.ModelAdmin):

    list_display = ('name','milk','color')
admin.site.register(cow_info_model,cow_info_admin)