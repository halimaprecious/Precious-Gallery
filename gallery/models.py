from django.db import models

# Create your models here.
class Location(models.Model):
    """
    A class for geographic loactions where a Photo could be taken
    """
    city = models.CharField(max_length=244)

    def __str__(self):
        return self.city

    def save_location(self):
        """
        A method to save the location name
        """
        return self.save()


            
class Category(models.Model):
    """
    A class for the category the Photo falls under
    """
    cat_name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.cat_name

    def save_category(self):
        """
        A method to save the category name
        """
        return self.save()

class Image(models.Model):
    """
    A class thaat determines how photos will be saved into the database
    """
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    post_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to ='photos/')

    def __str__(self):
        return self.name

    @classmethod
    def all_images(self):

        return Image.objects.all()

    @classmethod
    def search_by_category(cls,search_images):
        images = Image.objects.filter(categories__cat_name__icontains=search_images)
        return images

    @classmethod
    def view_location(cls,city):
        location = cls.objects.filter(location=city)
        return location

    @classmethod
    def view_category(cls,cat):
        categories = cls.objects.filter(categories=cat)
        return categories