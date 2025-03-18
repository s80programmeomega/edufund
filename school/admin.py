from .models import School
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


class BaseAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        if not change:  # If this is a new object (not an edit)
            obj.created_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(School)
class SchoolAdmin(BaseAdmin):
    list_display = ['name', 'id_number', 'location']
    search_fields = ['name', 'id_number']
    inlines = [
        StudentInline,
        RepresentativeInline,
        SchoolDocumentInline,
        SchoolImageInline,
    ]
    readonly_fields = ["created_by"]


@admin.register(FundingCampaign)
class FundingCampaignAdmin(BaseAdmin):
    list_display = ['name', 'amount', 'status',
                    'funding_progression', 'start_date', 'end_date']
    # Makes M2M fields easier to manage
    filter_horizontal = ['schools', 'sponsors']
    readonly_fields = ["created_by"]


@admin.register(Student)
class StudentAdmin(BaseAdmin):
    list_display = ['first_name', 'last_name', 'school']
    search_fields = ['first_name', 'last_name']
    list_filter = ['school']
    readonly_fields = ["created_by"]


@admin.register(Representative)
class RepresentativeAdmin(BaseAdmin):
    list_display = ['first_name', 'last_name', 'email', 'school']
    search_fields = ['first_name', 'last_name', 'email']
    list_filter = ['school']
    readonly_fields = ["created_by"]
