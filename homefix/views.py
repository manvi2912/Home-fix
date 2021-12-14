from django.contrib.messages.constants import DEFAULT_LEVELS
from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User
from homefix.forms import *
from django.contrib import messages
from homefix.models import *
from django.db.models import F, Count

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return render(request, 'index.html')
    else:
        user_type = User_type.objects.get(user=request.user)
        if user_type.user_type==1:
            return render(request, "index.html")
        else:
            return redirect('/mediator')

def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
       register_form = registerForm(request.POST)
       if register_form.is_valid():
           if register_form.check_password():
               if register_form.validate_password():
                   if register_form.username_unique():
                       if register_form.email_unique():
                           user = register_form.create_user()
                           post = User_type()
                           post.user_type=1
                           post.user = user
                           post.save()
                           messages.success(request, "User created successfully, Please login to avail services")
                           return redirect('/login')
                       else:
                            messages.error(request, "Email already exists!")
                   else:
                        messages.error(request, "Username already exists!")
               else:
                    messages.error(request, "Minimum 4 characters required in password")
           else:
                messages.error(request, "Password not matched")
       else:
           messages.error(request, "Please fill the form correctly")
       return redirect('/register')
                    
    else:
        return render(request, 'register.html')

def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method=="POST":
       login_form = loginForm(request.POST)
       if login_form.is_valid():
            if login_form.verify_and_login(request):
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password!")
       else:
            messages.error(request, "Invalid username or password!")
       return redirect('/login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect("/")

def area_service(request):
    if request.user.is_anonymous:
        return redirect("login")
    elif request.method=='POST':
        service = request.POST['service']
        area = request.POST['area']
        list_providers = Service_provider.objects.filter(service=service, area=area, max_no_services__gt=F('assigned_no_services'))
        reviews = Reviews.objects.filter(service_id__in = list_providers)
        if list_providers.exists():
            return render(request, 'service_request.html', {"Service_provider": list_providers, "Reviews": reviews})
        else:
            messages.error(request, "Service providers are not available at present.Please try again later!")
            return redirect('/')
    else:
        messages.error(request, 'Please choose the required service and area')
        return redirect('/')
    

def details(request):
    if request.method=='POST':
        service_id=request.POST['service_id']
        contact = request.POST['contact']
        requirement = request.POST['requirement']
        address = request.POST['address']
        s_provider = Service_provider.objects.get(pk=service_id)
        customer_name = request.user.first_name + " " + request.user.last_name
        status = 'Pending'
        new_request = Service_requested(customer_id=request.user, customer_name=customer_name, customer_contact_no=contact, address=address, requirement=requirement, service_id=s_provider, status=status)
        new_request.save()
        obj = Service_provider.objects.get(service_id=service_id)
        obj.assigned_no_services += 1
        obj.save()
        messages.success(request, "Your request has approved...your problem will be fixed soon")
        return redirect('/myservices')
    else:
        return redirect('/')

def contactus(request):
    if request.method=='POST':
        if request.user.is_anonymous:
            name = request.POST['name']
            email = request.POST['email']
            contact = request.POST['contact']
            desc = request.POST['requirement']
        else:
            contact = request.POST['contact']
            desc = request.POST['requirement']
            email = request.user.email
            name = request.user.first_name + " " + request.user.last_name
        contact_request = Contact_Us(name = name, contact_no=contact, email=email, desc=desc, status='Pending')
        contact_request.save()
        messages.success(request, "Your request for contact has been sent")
        return redirect('/contactus')
    else:
        return render(request, "contactus.html")

def myservices(request):
    if request.user.is_anonymous:
        return redirect("login")
    else:
        user_type = User_type.objects.get(user=request.user)
        if user_type.user_type == 2:
            return redirect('/')
        else:
            my_service=Service_requested.objects.filter(customer_id=request.user).order_by('date', 'status', 'id').reverse()
            return render(request, "myservices.html", {"Service_requested": my_service})

def cancel(request):
    if request.method=='POST':
        id = request.POST['cancel']
        req = Service_requested.objects.get(pk = id)
        req.status = "Canceled"
        req.save()
        req.service_id.assigned_no_services-=1
        req.service_id.save()
        return redirect('/myservices')
    else:
        return redirect('/')

def rating(request):
    if request.method=='POST':
        try:
            rating = request.POST['rating']
        except:
            messages.error(request, "Please give rating")
            return redirect('/myservices')
        id = request.POST['req_id']
        if rating:
            req = Service_requested.objects.get(pk = id)
            req.rated = rating
            req.save()
            req_services = Service_requested.objects.filter(service_id = req.service_id)
            sum=0
            count=0
            for i in req_services:
                if i.rated:
                   sum=sum+i.rated
                   count = count + 1
            provider = req.service_id
            provider.rating = sum/count
            provider.save()
            print(sum/count)
            return redirect('/myservices')
        else:
            messages.error(request, "Please give rating")
            return redirect('/myservices')
    else:
        return redirect('/')

def reviews(request):
    if request.method=="POST":
        service_id = request.POST['service_id']
        rating = request.POST['rating']
        review = request.POST['reviews']
        service_provider = Service_provider.objects.get(pk=service_id)
        new_review = Reviews(service_id = service_provider, customer_id = request.user, review=review, rating=rating)
        new_review.save()
        messages.success(request, "Thanks for giving review")
        return redirect('/myservices')
    else:
        return redirect('/myservices')

