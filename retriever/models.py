from django.db import models

# Create your models here.

class Tag(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True, unique=True)

    def __str__(self):
        return self.title

class TextSnippet(models.Model):

    title = models.CharField(max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    tag = models.ForeignKey(Tag, related_name='text_tag',null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title