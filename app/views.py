from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from app.models import hotel
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def homepage(request):
    blog=hotel.objects.all()
    return render(request,'index.html',{'hotel':blog,'user':request.user})
def detaillpage(request,id):
    blog=hotel.objects.get(id=id)
    return render(request,'detaills.html',{'blog':blog,'user':request.user})
def creatpage(request):
    if request.method=="GET":
        return render(request,"createform.html")
    else:
        hn=request.POST.get('hotel_name')
        hs=request.POST.get('hotel_des')
      
        r=request.POST.get('reviews')
        blog=hotel.objects.create(hotel_name=hn,hotel_des=hs,user=request.user,reviews=r)
        blog.save()
        return HttpResponse("hotel details created sucessfully")
def delete(request,id):
    blog=hotel.objects.get(id=id)
    if request.method=="POST":
        blog.delete()
        return redirect('homepage')
    return render(request,"delete.html",{'blog':blog})
def edit(request,id):
    blog=hotel.objects.get(id=id)
    if request.method=="POST":
        blog.hotel_name=request.POST['hotel_name']
        blog.hotel_des=request.POST['hotel_des']
        blog.reviews=request.POST['reviews']
        blog.save()
        return redirect('detailpage',id=blog.id)
    return render(request,'createform.html',{'blog':blog})
def userlogin(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect("/")
        else:
            return HttpResponse("user or password is not valid")
    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect("/")
        return render(request,'login.html')
def createuser(request):
    if request.method=="POST":
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        password=request.POST['password']
        email=request.POST['email']
        user=User.objects.create(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email
        )
        user.set_password(password)
        user.save()
        return HttpResponseRedirect("/")
    else:
        return render (request,"createuser.html")
def userlogout(request):
    logout(request)
    return HttpResponseRedirect("/") 
@login_required(login_url='/login')
def userprofile(request):
    return render(request, 'profile.html',{'user':request.user})

    
    


