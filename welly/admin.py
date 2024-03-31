from django.contrib import admin

# Register your models here.

from .models import Specialist, WorkList, Manager

admin.site.register(Specialist)
admin.site.register(WorkList)
admin.site.register(Manager)
