from django.contrib import admin

# Register your models here.


from webapp.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'created_task', 'dead_line', 'status']
    list_display_links = ['id', 'description']
    list_filter = ['status']
    search_fields = ['status', 'dead_line']
    fields = ['description', 'created_task', 'dead_line', 'status']
    readonly_fields = ['description', 'created_task']


admin.site.register(Task, TaskAdmin)