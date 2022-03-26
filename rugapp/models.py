from django.db import models

# Create your models here.

class NFTProject(models.Model):
    name = models.CharField(max_length=200, null=True)
    banner_image = models.CharField(max_length=2000, null=True)
    description = models.CharField(max_length=20000, null=True)
    total_volume = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    total_supply = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    num_owners = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    floor_price = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    slug = models.CharField(max_length=200, null=True)
    image = models.CharField(max_length=2000, null=True)
    external_link = models.CharField(max_length=2000, null=True)
    safelist_request_status = models.CharField(max_length=2000, null=True)
    credibility_rating = models.DecimalField(max_digits=8, decimal_places=1, null=True, default = 0)
    votes = models.IntegerField(null=True, default = 0)
