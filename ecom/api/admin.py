from django.contrib import admin

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price')
    list_filter = ('author', 'price')
    search_fields = ('title', 'author')
    ordering = ('author', 'price')
    fields = ('title', 'author', 'price')
    readonly_fields = ('title', 'author', 'price')
    list_per_page = 10
    list_max_show_all = 100
    list_editable = ('price',)
    list_display_links = ('title', 'author')
    list_select_related = ('author',)
    list_display_links_details = True
    list_display_links_details = 'title'
    list_display_links_details = 'author'
    list_display_links_details = 'price'
    list_display_links_details = 'author'
    
