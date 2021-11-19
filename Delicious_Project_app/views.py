from Delicious_Project_app.models import Feedback, IceCream,Order
from django.http.response import HttpResponse
from django.shortcuts import redirect, render,HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout




# Create your views here.

def Home(request):
    return render(request,'Delicious_Home.html')

def about(request):
    if request.method=="POST":
        feedback=request.POST.get('feedback')
        feedbackobj=Feedback(feedback=feedback)
        if feedback=='':
            messages.warning(request, 'Something wents wrong!')
        else:
            feedbackobj.save()
            messages.success(request, 'Your Feedback Submited Successfully!')
    
    return render(request,'Delicious_About.html')

def order(request):
    allProds=[]
    catprod=IceCream.objects.values('catagory','id')
    cats={item['catagory'] for item in catprod}
    for cat in cats:
        prod=IceCream.objects.filter(catagory=cat)
        n=len(prod)
        allProds.append([prod,range(1,n)])
    params={'allProds':allProds}
    
    if request.method=="POST":
        items_json=request.POST.get('items_json','')
        fname=request.POST.get('fname','')
        lname=request.POST.get('lname','')
        amount=float(request.POST.get('amount',''))
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        address=request.POST.get('address','')
        city=request.POST.get('city','')
        pincode=request.POST.get('pincode','')
        if amount < 100:
            messages.error(request,"Sorry we can't take the order below ₹ 100")
        else:
            order=Order(items_json=items_json,fname=fname,lname=lname,email=email,phone=phone,address=address,city=city,pincode=pincode,amount=amount)
            order.save()
            messages.success(request,"Your order is reach at your destnation only in 40 minutes, Thank You!") 
    return render(request,'Delicious_Order.html',params)

#Authentication Pages
def handlesignup(request):
    if request.method=='POST':
        #Get The Post Parameters
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        password=request.POST['password']
        #Check for errorneous inputs
        if len(username)>15:
            messages.warning(request, 'Username must be under 15 character!')
            return render(request,'Delicious_Login.html')
        if username.isalnum(): #alphanumeric
            messages.warning(request, 'Username must be alphanumeric ex: user@1,user_1,etc!')
            return render(request,'Delicious_Login.html')
        
        #create the user
        myuser=User.objects.create_user(username,email,password)
        myuser.first_name=fname
        myuser.last_name=lname
        # myuser.phone=phone
        # myuser.address=address
        # myuser.city=city
        myuser.save()
        messages.success(request, 'Successfully Signed In')
        return render(request,'Delicious_Login.html')
    else:
        return render(request,'Delicious_SignUp.html')

def userlogin(request):
    if request.method=='POST':
        loginusername=request.POST['loginusername']
        loginpass=request.POST['loginpass']
        user=authenticate(username=loginusername,password=loginpass)

        if user is not None:
            login(request,user)
            messages.success(request, str(user)+' logged in successfully! Now order some delicious ice creams.')
            return redirect('/order')
        else:
            messages.warning(request, 'Invalid username or password, Try again!')
            return render(request,'Delicious_Login.html')
    else:
        return render(request,'Delicious_Login.html')

def userlogout(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('/')
