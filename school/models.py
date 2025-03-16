
from django.db import models
from django.contrib.auth import get_user_model


class BaseModel(models.Model):
    created_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    date_added = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if hasattr(self, 'request') and not self.created_by:
            self.created_by = self.request.user
        return super().save(*args, **kwargs)


class School(BaseModel):
    id_number = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    # created_by = models.ForeignKey(
    #     get_user_model(), on_delete=models.CASCADE, related_name="schools",  blank=True, null=True)

    # date_added = models.DateTimeField(auto_now_add=True)
    # last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Representative(BaseModel):
    id_number = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    photo = models.ImageField(
        upload_to="images/school/representative/", blank=True)
    school = models.ForeignKey(
        "School", on_delete=models.CASCADE, related_name="representatives")

    # created_by = models.ForeignKey(
    #     get_user_model(), on_delete=models.CASCADE, related_name="school_representatives",  blank=True, null=True)

    # date_added = models.DateTimeField(auto_now_add=True)
    # last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Schools Representative"

    def __str__(self):
        return self.email


class Student(BaseModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    student_class = models.CharField(max_length=100, blank=True)
    student_story = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    photo = models.ImageField(upload_to="images/school/students/", blank=True)

    parent_consent = models.FileField(
        upload_to="documents/school/parent_consent/", blank=True
    )

    school = models.ForeignKey(
        "School", on_delete=models.CASCADE, related_name="students")

    # created_by = models.ForeignKey(
    #     get_user_model(), on_delete=models.CASCADE, related_name="students",  blank=True, null=True)

    # date_added = models.DateTimeField(auto_now_add=True)
    # last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email


class SchoolDocument(BaseModel):

    class DocumentType(models.TextChoices):
        ACCREDITATION_CERTIFICATE = 'ACCREDITATION_CERTIFICATE', 'Accreditation Ceritficate'
        APROOVAL_LETTER = 'APROOVAL_LETTER', 'Approval Letter'

    school = models.ForeignKey(
        "School", on_delete=models.CASCADE, related_name="documents")
    document = models.FileField(upload_to='documents/school/')
    type_of_document = models.CharField(
        max_length=100, choices=DocumentType.choices, default=DocumentType.ACCREDITATION_CERTIFICATE)

    # created_by = models.ForeignKey(
    #     get_user_model(), on_delete=models.CASCADE, related_name="school_documents",  blank=True, null=True)

    # date_added = models.DateTimeField(auto_now_add=True)
    # last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.school.name


class SchoolImage(BaseModel):

    school = models.ForeignKey(
        "School", on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to='images/school/')

    # created_by = models.ForeignKey(
    #     get_user_model(), on_delete=models.CASCADE, related_name="school_images",  blank=True, null=True)

    # date_added = models.DateTimeField(auto_now_add=True)
    # last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.school.name


class FundingCampaign(BaseModel):

    class FundingSatus(models.TextChoices):
        OPEN = "OPEN", 'open'
        CLOSE = "CLOSE", "close"

    name = models.CharField(max_length=150)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    reason = models.CharField(max_length=300, blank=True)
    description = models.TextField(blank=True)

    schools = models.ManyToManyField(
        to="School", related_name="funding_campaigns", blank=True,)
    sponsors = models.ManyToManyField(
        to="sponsor.Sponsor", related_name="funding_campaigns", blank=True)

    status = models.CharField(
        max_length=100, choices=FundingSatus.choices, default=FundingSatus.OPEN)

    # created_by = models.ForeignKey(
    #     get_user_model(), on_delete=models.CASCADE, related_name="funding_campaigns",  blank=True, null=True)

    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)

    # date_added = models.DateTimeField(auto_now_add=True)
    # last_modified = models.DateTimeField(auto_now=True)

    @property
    def funding_progression(self):
        progression = (self.donations.all().aggregate(models.Sum('amount'))[
                       'amount__sum'] / self.amount)*100 if self.donations.all() else 0
        anonymous_progression = (self.anonymous_donations.all().aggregate(models.Sum('amount'))[
            'amount__sum'] / self.amount)*100 if self.anonymous_donations.all() else 0
        total_progression = progression + anonymous_progression
        return f"{round(total_progression, 2)} %"

    def __str__(self):
        return self.name
