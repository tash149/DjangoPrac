from django.db import models
from django.conf import settings
# Create your models here.

User = settings.AUTH_USER_MODEL

class Post(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=120)
    # description = models.TextField()
    #authors_email = models.EmailField()
    #authors_email = models.OneToOneField('Author')
    # image = models.ImageField()
    # slug = models.SlugField()

    def __str__(self):
        return self.title

# class Author(models.Model):
#     user = models.ForeignKey(User)
#     email = models.EmailField()
#     cellphone_num = models.IntegerField()

#     def __str__(self):
#         return self.user.username
