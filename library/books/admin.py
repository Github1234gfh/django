from django.contrib import admin
from .models import Books, Category, Aply


admin.site.register(Category)

admin.site.register(Books)
admin.site.register(Aply)
