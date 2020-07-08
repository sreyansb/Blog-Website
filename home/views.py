from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from home.models import Contact
from django.contrib import messages
from blogapp.models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

#html pages
def home(request):
    allposts=Post.objects.all().order_by("-views")
    allposts=allposts[0:3]
    return render(request,"home/home.html",{'allposts':allposts})

def contact(request):
    if request.method=="POST":
        name=request.POST.get("name","")
        email=request.POST.get("email","")
        phone=request.POST.get("phone","")
        content=request.POST.get("content","")
        modelss=Contact(name=name,email=email,phone=phone,content=content)
        
        if len(name)<2 or len(email)<3 or len(phone)<8 or len(content)<4:
            messages.error(request,"Please give right credentials")
        else:
            modelss.save()
            messages.success(request,"Message has been sent successfully")
        #return render(request,'home/contact.html',)
    return render(request,'home/contact.html')

def about(request):
    return render(request,'home/about.html')

def search(request):
    query=request.POST['search']
    #only if query size is allowable just like google
    if len(query)>75:
        allposts=[]
    else:
        allposts1=Post.objects.filter(title__icontains=query)
        allposts2=Post.objects.filter(content__icontains=query)
        #distinct query sets
        allposts=(allposts1|allposts2).distinct()
    if len(allposts)==0:
        messages.warning(request,"No search results found")
    return render(request,'home/search.html',{'allposts':allposts,"query":query})

#authentication ke liye
def handlesignup(request):
    if request.method=='POST':
        username=request.POST.get("username","")
        fname=request.POST.get("fname","")
        lname=request.POST.get("lname","")
        email=request.POST.get("email","")
        pass1=request.POST.get("pass1","")
        pass2=request.POST.get("pass2","")
        if len(username)>10:
            messages.error(request,"Username must be under 11 characters")
            return redirect("home")
        
        if not(username.isalnum()):#alnum checks if special characters are not in username
            messages.error(request,"Username should have only letters and numbers")
            return redirect("home")

        if not(username.islower()):
            messages.error(request,"Username should have only letters and numbers")
            return redirect("home")

        try:
            if pass1!=pass2:
                raise Exception
        except Exception as e:
            messages.error(request,"Passwords are not same")
            return redirect("home")

        if not(pass1.isalnum()):
            messages.error(request,"PassWord should be alphanumeric")
            return redirect("home")

        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request,"User saved")
        return redirect('home')# the name of a url pattern
    else:
        raise Http404("Not allowed")

def handlelogin(request):
    if request.method=='POST':
        loginusername=request.POST['linusername']
        loginpassword=request.POST['lpass1']
        user=authenticate(username=loginusername,password=loginpassword)
        if user is not None:
            login(request,user)
            messages.success(request,"Successfully logged in")
            return redirect("home")
        else:
            messages.error(request,"Wrong Credentials")
            return redirect("home")
    raise Http404("Not allowed")

def handlelogout(request):
        logout(request)
        messages.success(request,"Successfully logged out")
        return redirect("home")
