from django.shortcuts import render
from django.contrib import messages
from .models import *
from django.db import transaction

def home(request):
    if request.method == 'POST':
        try:
            user_one = request.POST.get('user_one')
            user_two = request.POST.get('user_two')
            amount =  int(request.POST.get('amount'))
            with transaction.atomic():
                user_one_payment_obj = Payments.objects.get(user = user_one)
                user_two_payment_obj = Payments.objects.get(user = user_two)
                user_one_payment_obj.amount -= amount
                user_one_payment_obj.save()
                

                user_two_payment_obj.amount += amount
                user_two_payment_obj.save()
                
            messages.success(request,'Amount Transfered ')
        except Exception as e:
            messages.error(request,'Amount Transfered Failed ')            
            print(e)
    return render(request,'form.html')
