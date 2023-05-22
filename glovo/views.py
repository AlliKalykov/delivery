from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from .models import Order

def new_order(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            print(name, email, message)
            Order.objects.create(name=name, email=email, message=message)
            return HttpResponse("Thanks for contacting us!")
        else:
            return render(request, 'new_order.html', {'form': form})
    else:
        form = ContactForm()
        return render(request, 'new_order.html', {'form': form})


def order_detail(request, id):
    # .get() возвращает один объект,
    # но если объект не найден, то возбуждает исключение (ошибку)
    try:
        yuitgbd = Order.objects.get(id=id)
        return render(request, 'order_detail.html', {'order': yuitgbd})
    except Order.DoesNotExist:
        return HttpResponse('Заказ не найден')
    

def list_order(request):
    orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders': orders})
