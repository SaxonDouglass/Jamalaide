from django.contrib import admin

from blogs.models import *

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super(ArticleAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['author'].initial = request.user
        return form
