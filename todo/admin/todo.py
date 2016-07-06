from django.contrib import admin


class TodoAdmin(admin.ModelAdmin):
    fields = ('user', 'description', 'is_active', 'created_at')
    ordering = ('user', 'description', 'is_active', 'created_at')
