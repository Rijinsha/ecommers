from django.shortcuts import render
from ecommers_app.models import Product
from django.db.models import Q
# Create your views here.

def SearchResult(request):
    S_products=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        S_products=Product.objects.all().filter(Q(name__contains=query) )
    return render(request,'search.html',{'query':query,'products':S_products})
