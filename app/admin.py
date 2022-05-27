from django.contrib import admin

# Register your models here.
from app.models import TwitterUsernameNftMap

class TwitterUsernameNftMapAdmin(admin.ModelAdmin):
    list_display = ('twitter_username','token_id','is_following')

admin.site.register(TwitterUsernameNftMap,TwitterUsernameNftMapAdmin)