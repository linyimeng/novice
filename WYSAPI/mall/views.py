from django.shortcuts import render
# Create your views here.
def view_home(request):
    return render(request,"home.html")


def view_category_list(request):
    return render(request,"category_list.html")

def view_carts(request):
    return render(request,"carts.html")

def view_user_center(request):
    return render(request,"user_center.html")

def view_address(request):
    return render(request,"myaddress.html")

def add_address(request):
    if request.method=="GET":
        return render(request,"myaddress_add.html")
    else:
        pass

def view_order(request):
    return render(request,"myorder.html")

def view_mycollection(request):
    return render(request,"mycollection.html")


def view_detail(request):
    return render(request,"goodsdetail.html")


def view_confirm_order(request):
    return render(request,"confirm_order.html")



    