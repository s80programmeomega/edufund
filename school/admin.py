from django.contrib import admin

from .models import School, Representative, Student, SchoolDocument, SchoolImage

admin.site.register(School)
admin.site.register(Representative)
admin.site.register(Student)
admin.site.register(SchoolDocument)
admin.site.register(SchoolImage)
