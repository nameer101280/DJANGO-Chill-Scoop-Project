from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact

# Create your views here.
def index(request):
    context = {
        "variable1":"this is sent",
        "variable2":"My name is Nameer"
    }
    return render(request, 'index.html', context)
    #return HttpResponse("this is a home page")

def about(request):
    return render(request, 'about.html',)
    #return HttpResponse("this is about page")

def services(request):
    return render(request, 'services.html',)
    #return HttpResponse("this is a services page")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
    
    
    return render(request, 'contact.html',)
    #return HttpResponse("this is a contact page")
