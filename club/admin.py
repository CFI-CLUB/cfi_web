from django.contrib import admin
from club.models import Project, Category, Contactus, CFIProject

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'department', 'pass_year', 'publish',)
    list_editable = ('publish', )
    readonly_fields = ('created', 'views')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'author']
    list_filter = ('department', 'pass_year',)

class ContactusAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created', )
    readonly_fields = ('created',)
    search_fields = ['name', 'email']

class CFIProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'category', 'picture', )
    readonly_fields = ('created',)
    search_fields = ['title']



admin.site.register(Project, ProjectAdmin)
admin.site.register(Category)
admin.site.register(CFIProject, CFIProjectAdmin)
admin.site.register(Contactus, ContactusAdmin)