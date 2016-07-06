from django.contrib import admin
from todo.admin.user import UserAdmin
from todo.models import User

admin.site.register(User, UserAdmin)
