from django.contrib import admin
from fishbytes.models import Lake, Fish, Regulation, Catch, Tag

# Register your models here.
admin.site.register(Lake)
admin.site.register(Fish)
admin.site.register(Regulation)
admin.site.register(Catch)
admin.site.register(Tag)