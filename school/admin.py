from django.contrib import admin
from .models import School, Student, Representative, SchoolDocument, SchoolImage, FundingCampaign


class StudentInline(admin.TabularInline):  # or use admin.StackedInline
    model = Student
    extra = 1  # Number of empty forms to display


class RepresentativeInline(admin.TabularInline):
    model = Representative
    extra = 1


class SchoolDocumentInline(admin.TabularInline):
    model = SchoolDocument
    extra = 1


class SchoolImageInline(admin.TabularInline):
    model = SchoolImage
    extra = 1


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ['name', 'id_number', 'location']
    search_fields = ['name', 'id_number']
    inlines = [
        StudentInline,
        RepresentativeInline,
        SchoolDocumentInline,
        SchoolImageInline,
    ]


@admin.register(FundingCampaign)
class FundingCampaignAdmin(admin.ModelAdmin):
    list_display = ['name', 'amount', 'status',
                    'funding_progression', 'start_date', 'end_date']
    # Makes M2M fields easier to manage
    filter_horizontal = ['schools', 'sponsors']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'school']
    search_fields = ['first_name', 'last_name', 'email']
    list_filter = ['school']


@admin.register(Representative)
class RepresentativeAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'school']
    search_fields = ['first_name', 'last_name', 'email']
    list_filter = ['school']
