from django.contrib import admin
from .models import Role, ApplicationScope, Resource, Comment

admin.site.register(Role)
admin.site.register(ApplicationScope)
admin.site.register(Resource)
admin.site.register(Comment)
