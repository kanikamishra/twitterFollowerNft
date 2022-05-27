from django.db import models

# Create your models here.


class TwitterUsernameNftMap(models.Model):
    token_id = models.IntegerField(default=-1, unique=True, db_index=True)
    twitter_username = models.CharField(max_length=100)
    is_following = models.BooleanField(default=False)

