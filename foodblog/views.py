from django.shortcuts import render
from .models import *
from random import *
from django.core.mail import send_mail

# Create your views here.
def indexpage(request):
    return render(request,'foodblog/index.html')

def login_page(request):
    if 'email' in request.session:
            uid = User.objects.get(email=request.session['email'])
            return render(request,'foodblog/index.html',{'uid':uid})
    else:    
        return render(request,'foodblog/login.html') 

def registration_page(request):
    return render(request,'foodblog/registration.html')   

def register_user(request):
    try:
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['passowrd']

        insert = User.objects.create(username=username,email=email,password=password)

        if insert:
            print("---------------------------------------------------------------->Registration Successfully")
            s_msg = "Registration Successfully"
            send_mail('confirmation mail','welcome to foodblog','khushipatel284@gmail.com',[email])
            return render(request,'foodblog/login.html',{'s_msg':s_msg})  
        else:
            e_msg = "Please, Try Again"
            return render(request,'foodblog/registration.html',{'e_msg':e_msg})  
    except:
        e_msg = "Invalid Input"
        return render(request,'foodblog/registration.html',{'e_msg':e_msg})

def login_user(request):
    try:
        email = request.POST['email']
        password = request.POST['password']
        print("------------------>",email)
        print("------------------->",password)
        uid = User.objects.get(email = email)
        if uid:
            if uid.password==password:
                request.session['username']=uid.username
                request.session['id']=uid.id
                request.session['email']=uid.email
                return render(request,'foodblog/index.html',{'uid':uid})
            else:
                e_msg = "password does not match !"    
                return render(request,'foodblog/login.html',{'e_msg':e_msg})
        else:
            e_msg = "invalid user !"            
            return render(request,'foodblog/login.html',{'e_msg':e_msg})
    except:    
        e_msg = "user does not exist !"
        return render(request,'foodblog/login.html',{'e_msg':e_msg})


def logout(request):
    if 'email' in request.session:
        del request.session['username']
        del request.session['id']
        del request.session['email']
        e_msg = "Sign Out Successfully"
        return render(request,"foodblog/login.html",{'e_msg':e_msg}) 

    else:
        e_msg = "Sign Out Successfully"
        return render(request,'foodblog/login.html',{'e_msg':e_msg})       


def forgot_passsword(request):
    return render(request,'foodblog/forgot_password.html')        


def send_otp(request):
    try:
        email = request.POST['email']
        uid = User.objects.get(email=email)
        if uid:
            n_otp = randint(1111,9999)
            uid.otp = n_otp
            uid.save()

            send_mail('Your otp'+str(n_otp),'check your profile ','khushipatel284@gmail.com',[email])
            return render(request,'foodblog/reset_password.html',{'email':email})
        else:
            e_msg = "user does not exist !!"
            return render(request,'foodblog/forgot_password.html',{'e_msg':e_msg}) 
    except:   
        return render(request,'foodblog/forgot_password.html') 


def reset_password(request):
    try:
        email = request.POST['email']
        otp = request.POST['otp']
        newpassword = request.POST['newpassword']
        repassword = request.POST['repassword']
        uid = User.objects.get(email=email)
        if uid:
            if str(uid.otp) == str(otp) and newpassword==repassword:
                uid.password=newpassword
                uid.save()
                s_msg = "Password Updated Successfully"
                return render(request,'foodblog/login.html',{'s_msg':s_msg})
            else:
                e_msg = "otp or password does not same"
                return render(request,'foodblog/reset_password.html',{'e_msg':e_msg})
        else:
            e_msg='invalid user'
            return render(request,'foodblog/forgot_password.html')   
    except:
        e_msg = "user does not exist"
        return render(request,'foodblog/forgot_password.html',{'e_msg':e_msg})        

def profile_view(request):
    if 'email' in request.session:
        uid = User.objects.get(email=request.session['email'])
        return render(request,'foodblog/profile.html',{'uid':uid}) 

def update_profile(request):
    # pic = request.FILES['pic']
    return render(request,'foodblog/edit_profile.html')               

def foodgallary(request):
    try:
        data = Gallary.objects.all()
        if data:
            for i in data:
                print('======================================',i.pic)
            return render(request,"foodblog/foodgallary.html",{'data':data})
        else:
            return render(request,"foodblog/foodgallary.html")
    except:    
        return render(request,"foodblog/foodgallary.html")

def upload_gallary(request):
    try:
        pic = request.FILES['pic']
        uid = Gallary.objects.create(pic=pic)
        data = Gallary.objects.all()
        return render(request,"foodblog/foodgallary.html",{'data':data})

    except:    
        return render(request,"foodblog/index.html")


def review(request):
    return render(request,'foodblog/review.html')        
