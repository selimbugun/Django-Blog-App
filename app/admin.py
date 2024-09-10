from django.contrib import admin

from app.models import Category, Comment, Contact, Post, Tag, Projects

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish_date', 'author', 'is_home', 'is_active')
    readonly_fields = ('slug',)
    list_editable = ('is_home', 'is_active')

    list_filter = ('publish_date', 'author')
    search_fields = ('title', 'content')
    date_hierarchy = 'publish_date'



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    readonly_fields = ('slug',)
    list_filter = ('name',)
    search_fields = ('name',)



class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title',)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('username', 'subject', 'created')
    list_filter = ('created',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'created', 'active',)
    list_filter = ('active',)
    list_editable = ('active',)




admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Projects, ProjectAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Comment, CommentAdmin)