from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.





from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
from django.views.generic import CreateView

from .forms import MyModelForm
from .models import District, Place, MyModel
def home(request):

    return render(request,"index.html")


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request, "invalid credentials")
            return redirect('login')

    return render(request, "login.html")

def register(request):
    if request.method == 'POST':
        username = request.POST['username']

        password = request.POST['password']
        password1 = request.POST['password1']
        if password == password1:
            if User.objects.filter(username = username).exists():
                messages.info(request, "Username already exists")
                return  redirect ('register')


            else:
                user = User.objects.create_user(username = username,  password =password)
                user.save();
                return redirect('login')

        else:
            messages.info(request, "Password not match")
            return redirect('register')
        return redirect('/')

    return render(request, "register.html")


def form(request):
    district = request.GET.get('district')
    places = Place.objects.filter(district=district).all()
    return render(request, 'form.html', {'places': places})

def load_branches(request):
    district = request.GET.get('district')
    places = Place.objects.filter(district=district).all()
    return render(request, 'form.html', {'places': places})


class CreateMyModelView(CreateView):
    model = MyModel
    form_class = MyModelForm
    template_name = 'form.html'
    success_url = 'form.html'


def logout(request):
    auth.logout(request)
    return redirect('/')
