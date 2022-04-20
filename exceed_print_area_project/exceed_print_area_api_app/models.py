from django.db import models

# Create your models here.

class pdf_doc_table(models.Model):
    docfile = models.FileField()
