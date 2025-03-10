from django.db import models


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
    photo = models.ImageField(upload_to="school/students/photo")
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, related_name="representatives")
    date_added = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    photo = models.ImageField(upload_to="school/students/photo")

    school = models.ForeignKey(
        School, on_delete=models.CASCADE, related_name="students")

    date_added = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email


class SchoolDocument(models.Model):

    class DocumentType(models.TextChoices):
        ACCREDITATION_CERTIFICATE = 'ACCREDITATION_CERTIFICATE', 'Accreditation Ceritficate'
        APROOVAL_LETTER = 'APROOVAL_LETTER', 'Approval Letter'

    school = models.ForeignKey(
        School, on_delete=models.CASCADE, related_name="documents")
    document = models.FileField(upload_to='school/documents/')
    type_of_document = models.CharField(
        max_length=100, choices=DocumentType.choices, default=DocumentType.ACCREDITATION_CERTIFICATE)

    date_added = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)


class SchoolImage(models.Model):

    school = models.ForeignKey(
        School, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to='school/images/')

    date_added = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
