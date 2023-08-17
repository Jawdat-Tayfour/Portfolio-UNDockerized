from django.contrib import admin

from .models import Link,Image,Project


admin.site.register(Project)
admin.site.register(Image)
admin.site.register(Link)