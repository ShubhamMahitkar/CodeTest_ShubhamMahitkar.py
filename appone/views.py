from appone.models import RegistrationModel
from django.shortcuts import render, redirect
from appone.form import RegistrationForm
from django.views.generic.base import View
from django.conf import settings
from django.core.mail import send_mail


MAILCHIMP_APIKEY = settings.MAILCHIMP_API_KEY
MAILCHIMP_DATACENTER = settings.MAILCHIMP_DATACENTER
api_url = f"https://{MAILCHIMP_DATACENTER}.api.mailchimp.com/3.0"


class FirstPage(View):
    def get(self, request):
        return render(request, 'index.html')


class Login(View):
    def get(self, request):
        request.session['status'] = True
        return render(request, 'Login.html')

    def post(self, request):
        unm = request.POST['username']
        pas = request.POST['password']
        try:
            RegistrationModel.objects.get(uname=unm, password=pas)
            request.session['status'] = True
            return redirect('apply')

        except RegistrationModel.DoesNotExist:
            return redirect('login')


class Registration(View):
    def get(self, request):
        rm = RegistrationForm()
        return render(request, 'Registration.html', {"rm": rm})

    def post(self, request):
        if request.method == 'POST':
            request.session['status'] = True
            rf = RegistrationForm(request.POST)

            if rf.is_valid():
                rf.save()
                send_mail('MyWebsite.com', 'Welcome to our website', api_url, [rf.email])
                return redirect('Login.html')
            else:
                rm = RegistrationForm()
                return render(request, 'Registration.html', {'rm': rm})


def read_DB(request):
    rm = RegistrationModel.objects.all()
    return render(request, 'read_db.html', {"rm": rm})



def update(request):
    eid = request.GET["eid"]
    rm = RegistrationModel.objects.get(id=eid)
    return render(request, 'update.html', {"data": rm})


def updated(request):
    id = request.POST["id"]
    name = request.POST["t1"]
    dob = request.POST["t2"]
    address = request.POST["t4"]
    number = request.POST["t5"]
    mobile = request.POST["t5"]
    email = request.POST["t6"]
    uname = request.POST['t7']
    password = request.POST["t8"]
    am = RegistrationModel.objects.filter(id=id)
    am.update(name=name, password=password, dob=dob, address=address, number=number, uname=uname, email=email, mobile=mobile)
    return render(request, 'read_db.html', {"data":RegistrationModel.objects.all()})


def logout(request):
    del request.session['status']
    return redirect('index')


def delete(request):
    id = request.GET.get('id')
    nrf = RegistrationModel.objects.filter(id=id)
    nrf.delete()
    return redirect('delete')


def deleteuser(request):
    rm = RegistrationModel.objects.all()
    return render(request, 'delete.html', {"rm": rm})
