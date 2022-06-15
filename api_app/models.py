from django.db import models

# Create your models here.


class Notices(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=300, blank=True, null=True, default='')
