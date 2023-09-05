from django.contrib import admin 
from .models import Info
from .models import Upload_Item

class A(admin.ModelAdmin):
    list_display=("name","roll_no")
# Register your models here.
admin.site.register(Info,A)
admin.site.register(Upload_Item)