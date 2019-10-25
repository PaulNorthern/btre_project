from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator # пагинатор (1, 2, 3 стр.)
from .choices import price_choices, bedroom_choices, state_choices # словарь

# вытащим данные из БД (модели) и вставим затем их в наш шаблон
from .models import Listing

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True) # получаем все ранее объекты из БД по дате 
    #pip install pylint-django

    paginator = Paginator(listings, 6) # сколько элементов отображать на странице
    page = request.GET.get('page') # url-параметр, который мы ищем
    page_listings = paginator.get_page(page)


    context = {
        'listings': page_listings,
        
    }
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
                                #model   #pk  - for check is it exist
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing
    }

    return render(request, 'listings/listing.html', context)

def search(request):

    queryset_list = Listing.objects.order_by('-list_date')
    # Searching for keywords 
    if 'keywords' in request.GET: # not empty string
        keywords = request.GET['keywords']
        if keywords:
            # 'SQL...WHERE description LIKE....', выводим все что встречалось в описание 
            queryset_list = queryset_list.filter(description__icontains=keywords) 

    # City
    if 'city' in request.GET: # not empty string
        city = request.GET['city']
        if city:
            # 'SQL...WHERE city = variable'   
            queryset_list = queryset_list.filter(city__iexact=city) # iexact - case insensetive because [i]

    # State
    if 'state' in request.GET: # not empty string
        state = request.GET['state']
        if state:
            # 'SQL...WHERE city = variable'   
            queryset_list = queryset_list.filter(state__iexact=state)
    
    # Bedrooms
    if 'bedrooms' in request.GET: # not empty string
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            # 'SQL...WHERE bedrooms <= variable'   
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms) #LTE - less than 
    
    # Price
    if 'price' in request.GET: # not empty string
        price = request.GET['price']
        if price:
            # 'SQL...WHERE price = variable'   
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings': queryset_list,
        'values': request.GET, 
    }
    return render(request, 'listings/search.html', context)