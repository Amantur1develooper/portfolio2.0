from django.contrib import admin
from .models import *
# Register your models here.
class NameAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','work1','work2','work3','work4','work5','work6']

class MyworksAdmin(admin.ModelAdmin):
    list_display = ['id','name','title','link','image']
admin.site.register(Name, NameAdmin)
admin.site.register(Myworks, MyworksAdmin)
