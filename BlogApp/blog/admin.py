from django.contrib import admin
from .models import Category, Blog
from django.utils.safestring import mark_safe


class BlogAdmin(admin.ModelAdmin):
    list_display = ("blog_name", "homepage", "slug", "selected_categories",)
    list_editable = ("homepage",)
    search_fields = ("blog_name", "desc",)
    readonly_fields = ("slug",)
    list_filter = ("homepage", "categories",)

    def selected_categories(self, obj):
        html = "<ul>"

        for category in obj.categories.all():
            html += "<li>" + category.name + "</li>"

        html += "</ul>"
        return mark_safe(html)

admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
