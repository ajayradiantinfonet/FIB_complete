from django.contrib import admin
from .models import Question ,all_activity,Permission
# Register your models here.
admin.site.register(Question),
admin.site.register(all_activity),
admin.site.register(Permission),