from django.db import models


class Contribute(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    email = models.EmailField(max_length=1000)
    text = models.TextField(max_length=5000)
    timeStamp = models.DateTimeField(blank=True)
    slug = models.TextField(max_length=10)

    def __str__(self):
        return self.title
