from django.contrib import admin
from writer.models import Writer 

@admin.register(Writer)
class WriterAdmin(admin.ModelAdmin):
    list_display = ('name','nationality',)
    
