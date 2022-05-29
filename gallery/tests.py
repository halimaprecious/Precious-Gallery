from django.test import TestCase
from .models import  Location
# Create your tests here.

class LocationTestClass(TestCase):
    """
    Testing the Location class
    """
    def setUp(self):
        """
        Creating a new instance of the Location class
        """
        self.place = Location(city = "Nairobi")
        self.place.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.place, Location))

    def test_save_method(self):
        places = Location.objects.all()
        self.assertTrue(len(places) > 0)