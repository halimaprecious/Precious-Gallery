from django.db import models

# Create your models here.
class Location(models.Model):
    """
    A class for geographic loactions where a Photo could be taken
    """
    city = models.CharField(max_length=244)

    def __str__(self):
        """
        String representation
        """
        return self.city