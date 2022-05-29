from django.shortcuts import render
from .models import *
from django.http import Http404

# Create your views here.
def home(request):
    photos = Image.objects.all()
    city = Location.objects.all()
    category = Category.objects.all()

    if 'location' in request.GET and request.GET['location']:
        city = request.GET.get('location')
        photos = Image.view_location(city)

    elif 'category' in request.GET and request.GET['category']:
        category = request.GET.get('categories')
        photos = Image.view_category(category)

    return render(request, 'index.html', {"city":city,"photos":photos,"category":category })


def get_image_by_id(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except Image.DoesNotExist:
        raise Http404()
    return render(request,"details.html", {"image":image})

def search_results(request):

    if 'categories' in request.GET and request.GET['categories']:
        search_images = request.GET.get("categories")
        searched_images = Image.search_by_category(search_images)
        message = f"{search_images}"

        return render(request, 'find.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any image"
        return render(request, 'find.html',{"message":message})

