from django.db import models

class Document(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Chunk(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE, related_name='chunks')
    content = models.TextField()
    chunk_number = models.IntegerField()

class Reference(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    chunk = models.ForeignKey(Chunk, on_delete=models.CASCADE)
    url = models.URLField()


# Create your models here.
