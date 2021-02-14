from django.shortcuts import render , get_object_or_404
from .models import Blogging
# Create your views here.
def blogs(request):
    blogs = Blogging.objects.order_by('-date')
    return render(request, 'blogs.html' ,{'blogs':blogs})


def details(request , blog_id):
    blog = get_object_or_404(Blogging,pk=blog_id)
    return render (request, 'details.html', {'blog':blog})