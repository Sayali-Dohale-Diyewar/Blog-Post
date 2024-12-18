from django.contrib import admin
from .models import Posts,Comment, Reply, CustomUser
# Register your models here.
admin.site.register(Posts)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(CustomUser)
