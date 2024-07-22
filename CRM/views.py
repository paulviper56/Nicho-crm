from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import customers
from .forms import SignupForm
# Create your views here.

def homepage(request):
    customer = customers.objects.all()
    user = User.objects.all()
    context = {}
    context['customer'] = customer

    return render(request,'homepage.html',context)

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.info(request,"Login successful")
            return redirect('homepage')
        else:
            messages.info(request,"Invalid Credentials")
            return redirect('user_login')

    return render(request, 'user_login.html')

def user_logout(request):
    logout(request)
    return redirect('homepage')

def customer_registration(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        surname = request.POST['surname']
        username = request.POST['username']
        email = request.POST['email']
        address = request.POST['address']
        mobile_no = request.POST['mobile_no']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if customers.objects.filter(email=email).exists():
                messages.info(request,'email  already exist')
                return redirect('customer_registration')
            elif customers.objects.filter(username=username).exists():
                messages.info(request,'username already exist')
                return redirect('customer_registration')
            else:
                customer = customers.objects.create(firstname=firstname,surname=surname,username=username,email=email,address=address,mobile_no=mobile_no,password=password1)
                customer.save()
        else:
            messages.info(request,'passwords not match')
            return redirect('customer_registration')


    return render(request,'customer_registration.html',{'messages':messages})

def registration(request):
    if request.method == "POST" :
        form = SignupForm(request.POST)
        if form.is_valid() :
            form.save()
            # Authenticate
            username= form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, 'You have successfully registered')
                return redirect('homepage')
    else:
        form = SignupForm()

        return render(request, 'register.html', {'form':form})
    
    return render(request, 'register.html', {'form':form})