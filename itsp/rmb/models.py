from django.db import models
#import tsv1
# Create your models here.
class Status(models.Model):
    """docstring for Status."""
    title = models.CharField(max_length = 100)
    bill_status = models.TextField()
    updated_by = models.TextField()
    
    def __str__(self):
        return self.title
"""
experimental_data = output_sheet()
print(experimental_data)
"""
#Status.objects = output_sheet()
