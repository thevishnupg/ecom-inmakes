from django.shortcuts import render,get_object_or_404
from .models import Category,Product
from django.core.paginator import Paginator,EmptyPage,InvalidPage  # Paginator

from django.db.models import Q    # Search

# Create your views here.


def allproduct(request,c_slug=None):
    c_page = None
    roducts_list = None

    if c_slug!= None:
        c_page = get_object_or_404(Category,slug=c_slug)
        products_list = Product.objects.all().filter(category=c_page,avilable=True)
    else:
        products_list = Product.objects.all().filter(avilable=True)
    paginator = Paginator(products_list,8)
    try:
        page_number = request.GET.get('page') 
    except:
        page_number =1 
    try:
        products = paginator.page(page_number)
    except (EmptyPage,InvalidPage):
        products = paginator.page(paginator.num_pages)

    return render(request,"category.html",{'category':c_page,'products':products,'categ':products_list})

def productdetail(request,c_slug,product_slug):
    try:
        product = Product.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e
    return render(request,'product.html',{'product':product})

def search_product(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        products = Product.objects.filter(Q(name__contains=searched)|Q(category__name__contains=searched)|Q(description__contains=searched)|Q(price__contains=searched))

        return render(request, 'search.html', {'searched': searched, 'products': products})
    else:
        return render(request, 'search.html')