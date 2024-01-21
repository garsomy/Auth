from django.contrib import admin
from .models import Message, Themes, User

admin.site.register(Message)
admin.site.register(Themes)
admin.site.register(User)