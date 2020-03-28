from django.contrib import admin
from fishbytes.models import Lake, Fish, Regulation, Catch, Tag, Question

# Register your models here.
admin.site.register(Lake)
admin.site.register(Fish)
admin.site.register(Regulation)
admin.site.register(Catch)
admin.site.register(Tag)
admin.site.register(Question)