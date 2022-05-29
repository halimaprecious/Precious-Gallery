from django.test import TestCase
from .models import  Location, Category
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
    
    def tearDown(self):   
        '''
        delete test methods
        '''
        Location.objects.all().delete()
        Category.objects.all().delete()


class CategoryTestClass(TestCase):
    """
    Testing the Category class
    """
    def setUp(self):
        """
        Creating a new instance of the Category class
        """
        self.category = Category(cat_name = "Test")
        self.category.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_save_method(self):
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)