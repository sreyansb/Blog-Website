from django.contrib import admin
from .models import Post,BlogComment
# Register your models here.
admin.site.register(BlogComment)
# admin.site.register(Post)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js=('tiny.js',)

        
#or admin.site.register((Post,BlogComment))
