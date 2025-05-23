from django.contrib import admin
from django.contrib import admin
from .models import Document, Chunk, Reference

admin.site.register(Document)
admin.site.register(Chunk)
admin.site.register(Reference)


# Register your models here.
