from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.http.request import HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Items
from django.conf import settings
from django.contrib.auth.decorators import login_required
import stripe
from .forms import QuantityForm

stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.

def storefront_page(request, page_filter):
    if page_filter in ['drink', 'food']:
        store_items = Items.objects.filter(category=page_filter)
    else:
        store_items = Items.objects.all()
    context = {'items': store_items}
    return render(request, "storefront.html", context)

def pricing_view(request, product_id): 
    store_items = Items.objects.get(id=product_id)

    if request.method == "POST":
        form = QuantityForm(request.POST)

        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            return render(request,'pricing.html',{'item': store_items,
                                                'form': form,
                                                'quantity': quantity,
                                                })
        else:
            return render(request, 'pricing.html',{'item': store_items,
                                                'form': form,
                                                })
    else:
        form = QuantityForm()

    return render(request,'pricing.html',{'item': store_items,
                                        'form': form,
                                        })


def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        if User.objects.filter(username=username).exists():
            return render(request, "register.html", {
                "error": "Username already taken."
            })

        if User.objects.filter(email=email).exists():
            return render(request, "register.html", {
                "error": "Email already used."
            })

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        return redirect("login")
    return render(request, "register.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  
            return redirect("storefront")  
        else:
            return render(request, "login.html", {
                "error": "Invalid username or password."
            })

    return render(request, "login.html")

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def CreateCheckoutSessionView(request, product_id, quantity):
    product = Items.objects.get(id=product_id)

    YOUR_DOMAIN = f"{request.scheme}://{request.get_host()}"
    
    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': 'usd',
                    'unit_amount': int(product.price * 100) ,
                    'product_data': {
                        'name': product.name,
                        'images': [product.image]
                    },
                },
                'quantity': quantity,
            },
        ],
        metadata = {
            'product_id': product_id,
            'user_email': request.user.email
        },
        
        mode='payment',

        success_url=YOUR_DOMAIN + f'/payment-success/{product_id}/',
        cancel_url=YOUR_DOMAIN + f'/pricing/{product_id}/',
    )

    return redirect(checkout_session.url)

def payment_succesful(request, product_id):

    product = Items.objects.get(id=product_id)

    return render(request, 'payment-success.html', {'item': product})

def payment_failed(request, product_id):

    product = Items.objects.get(id=product_id)

    return render(request, 'payment-failed.html', {'item': product})



