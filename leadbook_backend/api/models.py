from django.db import models

# Create your models here.


class CompanyInfo(models.Model):
    company_name = models.CharField(max_length=256)
    security_code = models.CharField(max_length=256)
    office_address = models.TextField(null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    country = models.CharField(max_length=256,default="Indonesia")
    phone = models.TextField(null=True, blank=True)
    fax = models.TextField(null=True, blank=True)
    npwp = models.CharField(max_length=256, null=True, blank=True)
    site = models.URLField(max_length=200, null=True, blank=True)
    listing_date = models.DateField(null=True, blank=True)
    board = models.CharField(max_length=200, null=True, blank=True)
    business_field = models.TextField(null=True, blank=True)
    sector = models.CharField(max_length=256, null=True, blank=True)
    sub_sector = models.CharField(max_length=256, null=True, blank=True)
    registrar = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.company_name


class CorporateSecretary(models.Model):
    company = models.ForeignKey(
        CompanyInfo, related_name='secretaries', on_delete=models.CASCADE)
    name = models.CharField(max_length=256, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    phone = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Director(models.Model):
    company = models.ForeignKey(
        CompanyInfo, related_name='dicrectors', on_delete=models.CASCADE)
    name = models.CharField(max_length=256, null=True, blank=True)
    position = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return self.name
