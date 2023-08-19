from django.shortcuts import render,HttpResponse,redirect   #different ways of returning different output 
from django.contrib.auth.models import User     
from django.contrib.auth import authenticate,login,logout    #for checking user input password and username with database
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control,never_cache


# Create your views here.

#home page function 
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def index(request):
    return render(request,'index.html')


#about page function 
def about(request):
    return render(request,'about.html')

#contact page function
def contact(request):
    return render(request,'contact.html')



#login Page function 
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def handlelogin(request):
    if 'username' in request.session:
        return redirect('index')
    if request.method == "POST":
        uname = request.POST.get("username")
        pass1 = request.POST.get("pass1")
        myuser = authenticate(username=uname, password=pass1)
        print(myuser)
        if myuser is not None:
            login(request, myuser)
            request.session['username'] = uname
            messages.success(request, "Login Success")
            return redirect('/')
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('/login')
    return render(request, 'login.html')



#signUp page function 
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def handlesignup(request):
    #if 'username' in request.session:
    #    return redirect('index')
    if request.method=="POST":
        uname = request.POST['username']
        email = request.POST.get("email")
        password = request.POST.get("pass1")
        confirmpassword = request.POST.get("pass2")
        #print(uname,email,password,confirmpassword)

        if password != confirmpassword:
            messages.warning(request,"Password is Incorrect")
            return redirect('/signup')

        try:
            if User.objects.get(username=uname):
                messages.info(request,"Name Already Exist")
                return redirect('/signup')
        except:
            pass

        try:
            if User.objects.get(email=email):
                messages.info(request,"This Email already exist!")
                return redirect('/signup')
        except:
            pass
        
        myuser = User.objects.create_user(uname,email,password)
        myuser.save()
       # request.session['username'] = uname
        messages.success(request,"Signup Succesfully.Please login")
        return redirect('/login')
    return render(request,'signup.html')



# function for handling logout 

@login_required(login_url='/login')
def handlelogout(request):
    logout(request)
    messages.info(request,'Logout Success')
    return redirect('/login')