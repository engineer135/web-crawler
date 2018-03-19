from django.contrib import admin

# Register your models here.
from .models import BlogData

# BlogData를 admin 페이지에서 관리하겠다는 의미
admin.site.register(BlogData)