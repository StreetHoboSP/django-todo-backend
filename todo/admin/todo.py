from django.contrib import admin


class TodoAdmin(admin.ModelAdmin):
    fields = ('user', 'description', 'is_done', 'created_at')
    ordering = ('user', 'description', 'is_done', 'created_at')
