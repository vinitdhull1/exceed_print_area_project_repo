from django.contrib import admin
from .models import pdf_doc_table

# Register your models here.
@admin.register(pdf_doc_table)
class PdfDocTableAdmin(admin.ModelAdmin):
    list_display = ['id', 'docfile']
