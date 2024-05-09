from django.contrib import admin

from app.models import Author, JobPost, Location, Skills

class JobAdmin(admin.ModelAdmin):
    list_display = ('__str__','title','salary','posted_date', 'description')
    list_filter = ('posted_date','salary')
    search_fields = ('title',)
    search_help_text = "Write Your Query and hit Enter"
    # fields = (('title', 'description'),'salary')
    # exclude = ('slug',)
    # Syntax
    # fieldsets = (
        # '<section name here>',
    #     {
    #         'fields': ('field-1', 'field-2')
    #     }
    # )
    fieldsets = (
        (
            'Job Profile',
            {
                'classes':('collapse',),
                'fields': ('title', 'description')
            }
        ),
        (
            'More Information',
            {
                'classes':('collapse',),
                'fields': ('slug', ('salary', 'expiry_date'),)
            }
        ),
    )

# Register your models here.
admin.site.register(JobPost)
admin.site.register(Location)
admin.site.register(Author)
admin.site.register(Skills)