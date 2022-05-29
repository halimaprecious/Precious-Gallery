from django.test import TestCase
from .models import  Location, Category,Image

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

class ImageTest(TestCase):
    ''' def class instance setup for the image'''

    def setUp(self):
        self.nairobi = Location.objects.create(city='Nairobi')
        self.fiction = Category.objects.create(cat_name='fiction')
        self.mystery = Category.objects.create(cat_name='mystery')

        self.book = Image.objects.create(name='book', location=self.nairobi,  description='fiction book')
        self.book.categories.add(self.fiction)
        self.book.categories.add(self.mystery)

    # def a testcase for instance of the drinks class
    def test_instance(self):
        self.book.save()
        self.assertTrue(isinstance(self.book, Image))

    def test_delete_image(self):
        self.book.save()
        self.book.delete()
        self.assertTrue(len(Image.objects.all()) == 0)

    def test_update(self):
        self.book.save()
        self.book.name = 'fictionFacts'
        self.assertTrue(self.book.name == 'fictionFacts')

    def test_all_images(self):
        self.book.save()
        images = Image.all_images()
        self.assertTrue(len(images) > 0)

    def test_search_by_category(self):
        self.book.save()
        images = Image.search_by_category('fiction')
        self.assertTrue(len(images) > 0)

    def test_view_location(self):
        self.book.save()
        location = Image.view_location(self.nairobi)
        self.assertTrue(len(location) > 0)

    def test_view_category(self):
        self.book.save()
        categories = Image.view_category(self.mystery)
        self.assertTrue(len(categories) > 0)
