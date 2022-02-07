from django.utils import timezone
from django.db import models




# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=1000)
    created_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='post-img/')

    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'