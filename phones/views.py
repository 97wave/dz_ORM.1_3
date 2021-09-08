from django.http.request import HttpRequest
from phones.models import Phone
from django.shortcuts import render, redirect


def index(request):
    return redirect('catalog')


def show_catalog(request):
    content = Phone.objects.all()
    sort = request.GET.get('sort')
    sort_content = []
    sort_keys = []

    if sort == None:
        sort_content = content

    elif sort == 'name':
        for item in content:
            sort_keys.append(item.name)
        sorted_keys = sorted(sort_keys)
        for item in sorted_keys:
            sort_content.append(Phone.objects.get(name=item))
    
    elif sort == 'max_price' or sort == 'min_price':
        for item in content:
            sort_keys.append(item.price)
        sorted_keys = sorted(sort_keys)
        for item in sorted_keys:
            sort_content.append(Phone.objects.get(price=item))
        
        if sort == 'max_price':
            sort_content.reverse()

    template = 'catalog.html'
    context = {'phones' : sort_content}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {'phone' : Phone.objects.get(slug=slug)}
    return render(request, template, context)
