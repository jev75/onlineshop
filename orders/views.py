from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem, CartItem
from store.models import Clothing, Footwear, OtherProduct, Size
from .forms import BankTransferForm
from django.core.mail import send_mail
from django.http import Http404
from django.contrib import messages
from django.contrib.contenttypes.models import ContentType

# Užsakymo kūrimo funkcija
@login_required
def create_order(request):
    cart_items = CartItem.objects.filter(user=request.user)
    if request.method == 'POST':
        form = BankTransferForm(request.POST)
        if form.is_valid():
            order = Order.objects.create(
                user=request.user,
                is_paid=False,
                payment_method=form.cleaned_data['payment_method']
            )
            for item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=item.product.name,
                    quantity=item.quantity,
                    price=item.product.price
                )
            cart_items.delete()

            bank_details = {
                'paysera': 'Paysera sąskaita\nBankas: Paysera\nSąskaitos numeris: LT00 0000 0000 0000 0000',
                'swedbank': 'AB "Swedbank" bankas\nSąskaitos numeris: LT00 0000 0000 0000 0000',
                'seb': 'AB bankas "SEB"\nSąskaitos numeris: LT00 0000 0000 0000 0000',
                'luminor': 'Luminor\nSąskaitos numeris: LT00 0000 0000 0000 0000',
                'siauliu': 'AB "Šiaulių bankas"\nSąskaitos numeris: LT00 0000 0000 0000 0000',
                'revolut': 'Revolut (LT)\nSąskaitos numeris: LT00 0000 0000 0000 0000',
                'citadele': 'AS "Citadele bankas"\nSąskaitos numeris: LT00 0000 0000 0000 0000',
                'urbo': 'UAB Urbo bankas\nSąskaitos numeris: LT00 0000 0000 0000 0000',
                'lku': 'Lietuvos centrinė kredito unija\nSąskaitos numeris: LT00 0000 0000 0000 0000',
                'n26': 'N26 Bank (LT)\nSąskaitos numeris: LT00 0000 0000 0000 0000',
            }

            selected_bank_details = bank_details.get(form.cleaned_data['payment_method'], 'Bankas: Nenurodytas')

            send_mail(
                'Banko pavedimo instrukcijos',
                f'Sveiki {form.cleaned_data["full_name"]},\n\n'
                f'Dėkojame už jūsų užsakymą. Prašome atlikti mokėjimą šiais rekvizitais:\n\n'
                f'{selected_bank_details}\n'
                f'Mokėjimo paskirtis: Užsakymo numeris {order.id}\n\n'
                f'Pagarbiai,\n'
                f'Jūsų Komanda',
                'your-email@example.com',
                [form.cleaned_data['email']],
                fail_silently=False,
            )

            return redirect('orders:order_detail', order_id=order.id)
    else:
        form = BankTransferForm()
    return render(request, 'orders/order_create.html', {'cart_items': cart_items, 'form': form})

# Vartotojo užsakymų sąrašo atvaizdavimo funkcija
@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders/order_list.html', {'orders': orders})

# Funkcija, kuri atvaizduoja užsakymo detales
@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'orders/order_detail.html', {'order': order})

# Funkcija, kuri atvaizduoja vartotojo krepšelį
@login_required
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    valid_cart_items = [item for item in cart_items if item.product is not None]
    invalid_items = [item for item in cart_items if item.product is None]

    if invalid_items:
        for item in invalid_items:
            item.delete()
        messages.warning(request, 'Krepšelyje buvo elementų su netinkamais produktais, kurie buvo pašalinti.')

    total_price = sum(item.product.price * item.quantity for item in valid_cart_items)
    return render(request, 'orders/cart.html', {'cart_items': valid_cart_items, 'total_price': total_price})

# Dekoratorius, kuris reikalauja, kad vartotojas būtų prisijungęs
@login_required
def add_to_cart(request, product_id):
    # Patikriname, ar užklausa buvo pateikta POST metodu
    if request.method == 'POST':
        # Gauname produkto tipą iš POST užklausos
        product_type = request.POST.get('product_type')
        if product_type == 'clothing':
            model = Clothing
        elif product_type == 'footwear':
            model = Footwear
        elif product_type == 'otherproduct':
            model = OtherProduct
        else:
            raise Http404("Invalid product type")

        try:
            # Bandoma gauti produktą pagal jo ID
            product = model.objects.get(id=product_id)
        except model.DoesNotExist:
            raise Http404("Product does not exist")

        # Gauname produkto dydį iš POST užklausos, jei jis nurodytas
        size_id = request.POST.get('size')
        size = get_object_or_404(Size, id=size_id) if size_id else None

        # Gauname turinio tipą pagal produkto modelį
        content_type = ContentType.objects.get_for_model(product)
        # Bandoma sukurti arba gauti krepšelio elementą
        cart_item, created = CartItem.objects.get_or_create(
            content_type=content_type,
            object_id=product.id,
            user=request.user,
            defaults={'size': size}
        )
        if not created:
            # Jei krepšelio elementas jau egzistuoja, padidiname jo kiekį
            cart_item.quantity += 1
        else:
            # Jei krepšelio elementas naujas, nustatome jo kiekį ir dydį
            cart_item.quantity = 1
            cart_item.size = size
        cart_item.save()
        return redirect('orders:view_cart')
    else:
        raise Http404("Invalid request method")

# Funkcija, kuri pašalina prekę iš krepšelio
@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
    cart_item.delete()
    return redirect('orders:view_cart')