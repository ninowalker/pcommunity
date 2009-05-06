from django.db import models

# Create your models here.
class Auditable(models.Model):
    class Meta:
        abstract = True

    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User)
    updated = models.DateTimeField(auto_now=True)

    #TODO set current user

B_TAXA = ((0, 'Family'),(1,'Genus'),(2,'Species'),(3,'Subspecies'),(3,'Cultivar'),(2,'Hybrid'))

class Taxon(Auditable):
    parent = models.ForeignKey(Taxon, null=True)
    class_name = models.CharField(max_length=128, choices=B_TAXA)
    full_name = models.CharField(max_length=128)
    url = models.CharField(max_length=128)
    
    def save(self):
        self.url = ...
        self.full_name = ...
        super(Taxon, self).save()

    def get_absolute_url(self):
        pass

class CommonName(Auditable):
    name = models.CharField(max_length=128)
    taxon = models.ForeignKey(Taxon, related_name="common_names")
    lang_iso3 = models.CharField(max_length=3, default="eng")
    
    class Meta:
        unique_together = (('name','taxon'))

class PlantRef(Auditable):
    taxon = models.ForeignKey(Taxon, null=True)
    name = models.CharField(max_length=128)

class Community(Auditable):
    plants = models.ManyToManyField(PlantRef, related_name="communities")
    point
    area
    document

    
class 