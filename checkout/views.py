from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in you bag at the moment")
        return redirect(reverse, ('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51U6vPdHF9Vbq2m2QBbIddo6QHe9buyocJWR3bOR7fnF71VOpqv3rWt8m3F15XzfPCqT4g0Fw1oSs3C4XfMOgFP4r00iky5IHz3',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
