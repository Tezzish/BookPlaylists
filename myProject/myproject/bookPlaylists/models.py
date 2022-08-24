from django.db import models

class Books(models.Model):
    book_name = models.CharField(max_length=255)
    book_id = models.BigAutoField(primary_key=True)
    book_authorName = models.CharField(max_length=255)

