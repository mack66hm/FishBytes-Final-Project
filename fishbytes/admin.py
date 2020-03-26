from django.contrib import admin
from fishbytes.models import Lake, Fish, Regulation

# Register your models here.
admin.site.register(Lake)
admin.site.register(Fish)
admin.site.register(Regulation)