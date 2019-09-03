from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login
from .forms import IndexForm


# Create your views here.
def index(request):
    if request.method == 'POST':
        posts = IndexForm(request.POST)

        if posts.is_valid():
            #posts=form.save(commit=False)
            #posts.user=request.user
            #posts.save()

            # name=form.cleane_data['name']
            # email=form.cleane_data['email']
            # dob=form.cleane_data['dob']

            name  = request.POST.get('name')
            email = request.POST.get('email')
            dob = request.POST.get('dob')
            post=IndexForm(name=name,email=email,dob=dob)
            post.save()
            return redirect('display')
    else:
        posts = IndexForm()
    context = {'posts' : posts}
    return render(request,'user_example/index.html',context)

def display(request):
    posts=Index.objects.all()
    context={

        'name':posts[0].name
        #'email':posts[0].email
        #'dob':posts[0].dob
    }

    return render(request,'user_example/display.html',context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request,user)
            return redirect('index')
    else:
        form = UserCreationForm()
    context = {'form' : form}
    return render(request,'registration/register.html',context)



