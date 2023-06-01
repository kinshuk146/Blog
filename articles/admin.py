from django.contrib import admin
# Register your models here.
from .models import Article

#admin.site.register(Article)


@admin.register(Article)
class AdminArticle(admin.ModelAdmin):
    list_display=('title','published','author','slug')
    search_fields = ('title','description')
