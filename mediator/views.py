from django.contrib.messages.constants import DEFAULT_LEVELS
from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User
from django.contrib import messages
from homefix.models import *
from django.db.models import F, Count

def mediator(request):
    if request.user.is_anonymous:
        return redirect("medlogin")
    else:
        user_type = User_type.objects.get(user=request.user)
        if  user_type.user_type == 2:
            if request.method=="POST":
                status = request.POST['status']
                service = request.POST['service']
                area = request.POST['area']
                date = request.POST['date']
                if date:
                    service = Service_requested.objects.filter(status__contains = status, service_id__service__contains=service, service_id__area__contains=area, date=date).order_by('date').reverse()
                else:
                    service = Service_requested.objects.filter(status__contains = status, service_id__service__contains=service, service_id__area__contains=area).order_by('date').reverse()
                return render(request, "mediator.html", {"Service_requested": service})
            else:
                all_services = Service_requested.objects.all().order_by('date').reverse()
                return render(request, "mediator.html", {"Service_requested": all_services})
        else:
            return redirect("medlogin")

def medlogin(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method=="POST":
        username = request.POST['username']
        psw = request.POST['psw']
        user=auth.authenticate(username=username, password=psw)
        if user is not None:
            user_type = User_type.objects.get(user=user)
            if  user_type.user_type == 2:
                auth.login(request,user)
                return redirect("/")
            else:
                messages.error(request, "Invalid username or password!")
                return redirect("medlogin")
        else:
            messages.error(request, "Invalid username or password!")
            return redirect("medlogin")
    else:
        return render(request, 'medlogin.html')

def logout(request):
    auth.logout(request)
    return redirect("medlogin")

def allcontact(request):
    if request.user.is_anonymous:
        return redirect("medlogin")
    else:
        user_type = User_type.objects.get(user=request.user)
        if  user_type.user_type == 2:
            if request.method=="POST":
                status = request.POST['status']
                date = request.POST['date']
                if date:
                    contact = Contact_Us.objects.filter(status__contains = status, date=date).order_by('date').reverse()
                else:
                    contact = Contact_Us.objects.filter(status__contains = status).order_by('date').reverse()
                return render(request, 'contact_details.html', {"Contact_Us": contact}) 
            else:
                contact = Contact_Us.objects.all().order_by('date').reverse()
                return render(request, 'contact_details.html', {"Contact_Us": contact}) 
        else:
            return redirect("medlogin")

def service_providers(request):
    if request.user.is_anonymous:
        return redirect("medlogin")
    else:
        user_type = User_type.objects.get(user=request.user)
        if  user_type.user_type == 2:
            if request.method=="POST":
                area = request.POST['area']
                service = request.POST['service']
                if area and service:
                    list_providers = Service_provider.objects.filter(area = area, service = service)
                elif area:
                    list_providers = Service_provider.objects.filter(area = area)
                elif service:
                    list_providers = Service_provider.objects.filter(service = service)  
                else:
                    list_providers = Service_provider.objects.all()
                return render(request, "service_providers.html", {"Service_provider": list_providers})  
            else:
                list_providers = Service_provider.objects.all()
                return render(request, "service_providers.html", {"Service_provider": list_providers})
        else:
            return redirect("medlogin")

def contact_status(request):
    if request.method=="POST":
        status = request.POST['change_status']
        id = request.POST['id']
        contact = Contact_Us.objects.get(pk=id)
        contact.status = status
        contact.save()
        return redirect("allcontact")
    else:
        return redirect("allcontact")

def service_status(request):
    if request.method=="POST":
        status = request.POST['change_status']
        id = request.POST['id']
        req = Service_requested.objects.get(pk = id)
        req.status = status
        req.save()
        return redirect('/')
    else:
        return redirect('/')
       
def reset(request):
    if request.method == "POST":
        count = Service_requested.objects.filter(status="Pending").values('service_id').order_by('service_id').annotate(pending=Count('service_id'))
        service_providers = Service_provider.objects.all()
        dict = {}
        for i in count:
            dict[i['service_id']] = i['pending']
        for i in service_providers:
            if i.service_id in dict:
                i.assigned_no_services = dict[i.service_id]
            else:
                i.assigned_no_services = 0
            i.save()
        return redirect('service_providers')
    else:
        return redirect('service_providers')