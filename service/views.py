from django.shortcuts import render
from .models import  Category, Models
from django.views.generic import ListView

class CategoryList(ListView):
    model = Category
    queryset = Category.objects.all()
    context_object_name = 'categories'
    template_name = 'base.html'

# Create your views here.
