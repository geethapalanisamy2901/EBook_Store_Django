from django.contrib import admin

# Register your models here.
from preview import models

class BookDetailsAdmin(admin.ModelAdmin):
	list_display=('book_name','author','description','price','rating')
admin.site.register(models.BookDetails, BookDetailsAdmin)
class UserDetailsAdmin(admin.ModelAdmin):
	list_display=('name','email')
admin.site.register(models.UserDetails, UserDetailsAdmin)