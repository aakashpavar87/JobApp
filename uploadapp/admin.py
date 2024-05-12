from django.contrib import admin

from uploadapp.models import UploadFile, Uploads

# Register your models here.
admin.site.register(Uploads)
admin.site.register(UploadFile)
