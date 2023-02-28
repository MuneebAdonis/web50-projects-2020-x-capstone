from django.contrib import admin

from .models import User,Stain,Tissue,Slide,Gender,Title, System, Diagnosis, Comment

# Register your models here.
admin.site.register(User)
admin.site.register(Stain)
admin.site.register(System)
admin.site.register(Tissue)
admin.site.register(Gender)
admin.site.register(Slide)
admin.site.register(Title)
admin.site.register(Diagnosis)
admin.site.register(Comment)