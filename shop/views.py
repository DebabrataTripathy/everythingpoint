from django.shortcuts import render
from.models import Products,Order
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    product=Products.objects.all()
    item_name=request.GET.get('i_name')
    if item_name!="" and item_name is not None:
        product=product.filter(name__icontains=item_name)
    paginator=Paginator(product,3)
    page=request.GET.get('page')
    product=paginator.get_page(page)
    return render(request,"shop/index.html",{"products":product})
def detail(request,id):
    product=Products.objects.get(id=id)
    return render(request, "shop/detail.html",{"product":product})

def checkout(request):
    if request.method=="POST":
        items=request.POST.get("items","")
        print(items)
        name=request.POST.get("name","")
        email=request.POST.get("email","")
        address=request.POST.get("address","")
        city=request.POST.get("city","")
        state=request.POST.get("state","")
        zip=request.POST.get("zip","")
        total=request.POST.get("total_amt","")

        order=Order(items=items,name=name,email=email,address=address,city=city,state=state,zip=zip,total=total)
        order.save()


    return render(request,"shop/checkout.html")