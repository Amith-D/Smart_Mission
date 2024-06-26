from django.shortcuts import render
from basic_app.forms import UserForm,UserProfileInfoForm,Contact
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.

def search(request):
    return render(request, 'basic_app/search.html')
    
def index(request):
    return render(request,'basic_app/index.html')

def about(request):
    return render(request,'basic_app/about.html')

def contact(request):
    form = Contact(request.POST or None)
    if form.is_valid():
        form.save()
        form = Contact()
    return render(request,'basic_app/contact.html',{'cont':form})
    
@login_required
def home(request):
    return render(request,'basic_app/navmenu.html')

@login_required
def  dean_login(request):
    return render(request,'basic_app/menu.html')



@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def form_fill(request):
    return render(request, 'basic_app/form.html')

def archive(request):
    return render(request, 'basic_app/archive.html')


def register(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit = False)
            profile.user =user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()


    return render(request,'basic_app/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})



def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('basic_app:home'))
            else:
                return HttpResponse("Account NOT Active")
        else:
            print("Danger")
            print("Username:{} and password {}".format(username,password))
            messages.error(request,'Username or Password Invalid')
            return render(request,'basic_app/userlogin.html')
    else:
        return render(request,'basic_app/userlogin.html',{})
