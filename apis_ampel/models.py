from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from apis_core.apis_entities.models import TempEntityClass

class AmpelGeneric():
    pass
# class AmpelGeneric(models.Model):
#     ampel_choices = [
#         ("red", "red"),
#         ("yellow", "yellow"),
#         ("green", "green"),
    
#     ]

#     class Meta:
#         unique_together = [["object_id", "content_type"]]

#     content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
#     object_id = models.PositiveIntegerField()
#     content_object = GenericForeignKey('content_type', 'object_id')
    
#     status = models.CharField(max_length=300, choices=ampel_choices, default="red")
#     note = models.TextField(max_length=2000, null=True, blank=True)

#     def __str__(self):
#         return f"Ampel [{self.status}] - {str(self.content_object)}"

class AmpelTemp(models.Model):
    #TODO: rename to Ampel
    ampel_choices = [
    ("red", "red"),
    ("yellow", "yellow"),
    ("green", "green"),

    ]

    temp_entity = models.OneToOneField(TempEntityClass, on_delete=models.CASCADE, related_name="ampel", primary_key=True)
    status = models.CharField(max_length=300, choices=ampel_choices, default="red")
    note = models.TextField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return f"Ampel [{self.status}] - {str(self.temp_entity)}"


class AmpelSettings(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    active = models.BooleanField(null=False, blank=False, default=False)

    
        
