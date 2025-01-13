from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from app.models import hotel,room,book,user_profile,RoomImage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


def homepage(request):
    blog=hotel.objects.all()
    return render(request,'index.html',{'hotel':blog,'user':request.user})
def detaillpage(request,id):
    blog=hotel.objects.get(id=id)
    return render(request,'detaills.html',{'blog':blog,'user':request.user})
@login_required(login_url='/login')
def creatpage(request):
    
    if request.method=="GET":
        return render(request,"createform.html")
    else:
        hn=request.POST.get('hotel_name')
        hs=request.POST.get('hotel_des')
      
        r=request.POST.get('reviews')
        profile_pic = request.FILES['profile_pic']

        blog=hotel.objects.create(hotel_name=hn,hotel_des=hs,user=request.user,reviews=r,profile_pic=profile_pic)
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
        blog.profile_pic=request.FILES['profile_pic']
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
        phonenumber=request.POST['phonenumber']
        
        is_vendor = request.POST.get('is_vendor', False) 
        if User.objects.filter(username=username).exists():
            return HttpResponse("Error: Username already exists. Please enter another username.")
        user=User.objects.create(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email
        )
        user.set_password(password)
        user.save()
        profile=user_profile.objects.create(
            user=user,
            phonenumber=phonenumber,
            is_vendor=is_vendor
        )        
        profile.save()
        return HttpResponseRedirect("/")
    else:
        return render (request,"createuser.html")
    
def userlogout(request):
    logout(request)
    return HttpResponseRedirect("/") 
@login_required(login_url='/login')
def userprofile(request):
    return render(request, 'profile.html',{'user':request.user})

def roomadd(request,id):
    _hotel=hotel.objects.get(id=id)

    if request.method=="POST":
        room_number=request.POST['room_number']
        room_type=request.POST['room_type']
        price_per_night=request.POST['price_per_night']
        is_available=request.POST['is_available']
        room_des=request.POST['room_des']
        room_pic=request.FILES.getlist('room_pic')
        if room.objects.filter(room_number=room_number).exists():
            return HttpResponse(f"Error: Room number {room_number} already exists. Please choose another room number.")
        blog=room.objects.create(
            room_number=room_number,
            room_type=room_type,
            price_per_night=price_per_night,
            is_available=is_available,
            hotel = _hotel,
            room_des=room_des)
            # room_pic=room_pic)
        blog.save()
        for img in room_pic:
            images= RoomImage.objects.create(room=blog,room_pic=img)
        return HttpResponse("Your room has been added successfully!")
    
    return render(request,'room.html')
def chooseroom(request, id):
    _hotel = hotel.objects.get(id=id)
    rooms = room.objects.filter(hotel=_hotel)  
    return render(request, 'roomdetail.html', {'rooms': rooms, 'user': request.user})

@login_required(login_url='/login')  
def booknow(request, id):
    room1 = room.objects.get(id=id)
    hotel1 = room1.hotel 
    if request.method == "POST":
        check_in_date = request.POST['check_in_date']
        check_out_date = request.POST['check_out_date']
        number_of_guest = request.POST['number_of_guest']
        booking_date = request.POST['booking_date'] 
    
        if request.user.is_authenticated:
            booking = book.objects.create(
                user=request.user,
                hotel=hotel1,
                room=room1,
                check_in_date=check_in_date,
                check_out_date=check_out_date,
                number_of_guest=number_of_guest,
                booking_date=booking_date
            )
            booking.save()
            room1.is_available=False

            room1.save()
            return HttpResponse("Your room is booked!")
        else:
            return HttpResponse("You must be logged in to book a room.")
    
    return render(request, 'booknow.html', {'room': room1})
def editroom(request,id):
    edit=room.objects.get(id=id)
    if request.method=="POST":
        room_pic=request.FILES.getlist('room_pic')
        edit.room_number=request.POST['room_number']
        edit.room_type=request.POST['room_type']
        edit.price_per_night=request.POST['price_per_night']
        edit.is_available=request.POST['is_available']
        edit.room_des=request.POST['room_des']
        edit.room_pic=request.FILES.getlist('room_pic')
        edit.save()
        for img in room_pic:
            images= RoomImage.objects.create(room=edit,room_pic=img)
            images.save()
            return HttpResponse("Your room has been edded successfully!")
        
       
    return render(request,'room.html',{'edit':edit})
def delroom(request,id):
    image_ids = request.POST.getlist('room_pic')
    for _id in image_ids:
        img = RoomImage.objects.get(id=_id)
        img.delete()
    return HttpResponse("your pic deleted sucesfully")

    # return HttpResponseRedirect('room.html')



   



        

        

