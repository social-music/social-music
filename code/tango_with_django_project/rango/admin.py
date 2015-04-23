from django.contrib import admin
from rango.models import UserModel, StreamModel, ContentModel

# Register your models here.
admin.site.register(UserModel)
admin.site.register(StreamModel)
admin.site.register(ContentModel)