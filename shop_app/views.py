from django.shortcuts import render
from .models import Category, Product
import sqlite3
# Create your views here.
def index(request):
    cat = Category.objects.all()
    prod = Product.objects.all()[:4]
    return render(request , "index.html", {'categories' : cat, 'products' : prod, "count": len(prod)})


def cart(request):
    return render(request , "cart.html")
def dashboard(request):
    return render(request , "dashboard.html")
def order_complete(request):
    return render(request , "order_complete.html")
def place_order(request):
    return render(request , "place-order.html")
def product_detail(request):
    return render(request , "product-detail.html")
def register(request):
    return render(request , "register.html")
# def search_result(request):
#     ser = request.GET.get("q", "").strip()
#     # prod = Product.objects.none()
#     prod = Product.objects.all().filter(product_name__icontains=ser)
#     return render(request , "search-result.html", {'result' : prod, "count": len(prod)})

def search_result(request):
    ser = request.GET.get("q", "").strip()
    cat = Category.objects.all()
    with sqlite3.connect('db.sqlite3') as conn:
        cursor = conn.cursor()
        query = "SELECT * FROM tbl_products WHERE product_name LIKE ?"
        cursor.execute(query, [f"%{ser}%"])
        rows = cursor.fetchall()
        rows = [Product(*row) for row in rows]
    return render(request , "search-result.html", {'categories' : cat,'result' : rows, "count": len(rows)})

def signin(request):
    return render(request , "signin.html")
def store(request):
    cat = Category.objects.all()
    prod = Product.objects.all()
    return render(request , "store.html", {'categories' : cat, 'result' : prod, "count": len(prod)})
