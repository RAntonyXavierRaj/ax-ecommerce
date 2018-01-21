from django.shortcuts import render, redirect

from products.models import Product
from .models import Cart


"""
def cart_create(user=None):
    cart_obj = Cart.objects.create(user=None)
    print("New cart created")
    return cart_obj
"""


def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    return render(request, "carts/home.html", {"cart": cart_obj})


def cart_update(request):
    product_id = request.POST.get('product_id')
    if product_id is not None:
        try:
            product_obj = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            print("Show message to user, product is gone?")
            return redirect("cart:home")
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        if product_obj in cart_obj.products.all():
            cart_obj.products.remove(product_obj)
        else:
            cart_obj.products.add(product_id)
        request.session['cart_items'] = cart_obj.products.count()
        #cart_obj.title = "add"
        #cart_obj.save()
        #cart_obj.products.remove(product_obj)
        #return redirect(product_obj.get_absolute_url())
    return redirect("cart:home")

"""
    #del request.session['cart_id']
    cart_id = request.session.get("cart_id", None)
    #if cart_id is None: # and isinstance(cart_id, int):
        #cart_obj = cart_create()  # create a brand new cart
        #request.session['cart_id'] = cart_obj.id
        #print("New cart created")
    #else:
    qs = Cart.objects.filter(id=cart_id)
    if qs.count() == 1:
        #print("Cart ID exists")
        cart_obj = qs.first()
        if request.user.is_authenticated and cart_obj.user is None:
            cart_obj.user = request.user
            cart_obj.save()
    else:
        cart_obj = Cart.objects.new(user=request.user)   #print(cart_id)
        request.session['cart_id'] = cart_obj.id
    #cart_obj = Cart.objects.get(id=cart_id)

# print(request.session)
# print(dir(request.session))
# request.session.set_expiry(300) # 5 minutes
# request.session.session_key
# key = request.session.session_key
# print(key)
# setter
# request.session['user'] = request.user.username """