from django.contrib import admin

from acceuil.models import Acceuilperso, Contenus, BlogImage, Visite


class BlogImageInline(admin.TabularInline):
	model = BlogImage
	extra = 1

class ContenusAdmin(admin.ModelAdmin):
	inlines = [BlogImageInline]

admin.site.register(Contenus, ContenusAdmin)
admin.site.register(Acceuilperso)
admin.site.register(BlogImage)
admin.site.register(Visite)
