from django.contrib import admin
from blog.models import Category, Post, PostSection, SectionType

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'state', 'created_on')
    date_hierarchy = 'created_on'
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

class PostSectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'title', 'type', 'created_on')
    date_hierarchy = 'created_on'
    pass

class SectionTypeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(PostSection, PostSectionAdmin)
admin.site.register(SectionType, SectionTypeAdmin)