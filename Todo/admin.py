from django.contrib import admin
from GTD.Todo.models import Todo,User

class TodoAdmin(admin.ModelAdmin):
    list_diplay=('subject','date','priority')

class UserAdmin(admin.ModelAdmin):
    list_display=('user','password')

admin.site.register(Todo,TodoAdmin)
admin.site.register(User,UserAdmin)
