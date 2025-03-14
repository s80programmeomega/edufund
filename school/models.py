
from django.db import models
from decimal import Decimal


class School(models.Model):
    id_number = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    date_added = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Representative(models.Model):
    id_number = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    photo = models.ImageField(
        upload_to="images/school/representative/", blank=True)
    school = models.ForeignKey(
        "School", on_delete=models.CASCADE, related_name="representatives")
    date_added = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Schools Representative"

    def __str__(self):
        return self.email


class Student(models.Model):
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

    date_added = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email


class SchoolDocument(models.Model):

    class DocumentType(models.TextChoices):
        ACCREDITATION_CERTIFICATE = 'ACCREDITATION_CERTIFICATE', 'Accreditation Ceritficate'
        APROOVAL_LETTER = 'APROOVAL_LETTER', 'Approval Letter'

    school = models.ForeignKey(
        "School", on_delete=models.CASCADE, related_name="documents")
    document = models.FileField(upload_to='documents/school/')
    type_of_document = models.CharField(
        max_length=100, choices=DocumentType.choices, default=DocumentType.ACCREDITATION_CERTIFICATE)

    date_added = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.school.name


class SchoolImage(models.Model):

    school = models.ForeignKey(
        "School", on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to='images/school/')

    date_added = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.school.name


class FundingCampaign(models.Model):

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

    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)

    date_added = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

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
