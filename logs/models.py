from django.db import models


# Create your models here.
class Topic(models.Model):
    title = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Entry(models.Model):
    topic_id = models.ForeignKey(Topic, on_delete=models.CASCADE)
    #topic = Topic.title
    date_added = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    class Meta:
        verbose_name_plural="Entries"

    def __str__(self):
        return f"{self.text[:50]}..."



