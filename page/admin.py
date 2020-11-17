from django.contrib import admin
from .models import Page,Carousel
# Register your models here.



class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    
    list_display = (    #Gruplandırma
        "pk",
        'title', 
        "slug",  
        'status',
        "update_at",
                    
    )
    list_filter = ("status",)
    list_editable = (
        "status",
        "title",

    
    )

class CarouselAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "title",
        "cover_image",
        "status",

    ]



admin.site.register(Page, PageAdmin)
admin.site.register(Carousel)