from django.contrib import admin

# Register your models here.
from . models import Notes, SharedNotes
admin.site.register(Notes)
admin.site.register(SharedNotes)