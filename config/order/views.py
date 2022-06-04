from django.shortcuts import render, get_object_or_404, redirect
from .models import Order
from book.models import Book
from django.contrib.auth.decorators import login_required


@login_required
def orders_list(request):
    orders = Order.objects.filter(user=request.user, is_reserve=True)
    context = {
        'orders':orders
    }
    return render(request, 'order/orders.html', context)

@login_required
def order_delete(request, pk):
    order = get_object_or_404(Order, user=request.user, pk=pk)
    book = get_object_or_404(Book, pk=order.book.id)
    book.reserve=False
    book.save()
    order.is_reserve=False
    order.save()
    return redirect('order:my-orders')

@login_required
def order_create(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if book.reserve:
        return redirect('order:my-orders')
    order = Order.objects.create(user=request.user,book=book)
    order.save()
    book.reserve=True
    book.save()
    return redirect('order:my-orders')