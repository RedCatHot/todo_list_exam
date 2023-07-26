from django.contrib import admin

from ToDo.models import Tag, Task


@admin.register(Task)
class TagAdmin(admin.ModelAdmin):
    list_display = ["content", "created_datetime", "deadline_datetime", "is_done"]
    list_filter = ["created_datetime"]
    search_fields = ["content"]


admin.site.register(Tag)
