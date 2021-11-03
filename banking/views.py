from django.shortcuts import render
from .models import details
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def home(request):
    detail = details.objects.all()
    if request.method == 'POST':
        amount = int(request.POST['amount'])
        sender = request.POST['sender']
        reciever = request.POST['reciever']
        data_sender = details.objects.all().filter(name = sender)[0]
        data_reciever = details.objects.all().filter(name = reciever)[0]
        if amount< data_sender.balance:
            data_sender.balance -= amount
            data_reciever.balance += amount
            data_reciever.save()
            data_sender.save()
        else:
            return render(request, 'error.html')
        print(sender,reciever)
    return render(request, 'index.html', {'details': detail})