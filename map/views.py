from django.shortcuts import render
from geopy.geocoders import Nominatim
# Create your views here.
from map.forms import MapForm,UserRegisterForm
from map.models import shape_data
from django.contrib.auth.decorators import login_required



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html',{'form':form})




def map(request):
    l = []

    d = {}
    shape_detail = shape_data.objects.all()
    username = "Niranjan"
    d["name"] = username
    pincode = 121004
    real_add = str("2554/A") + " " +str("60 foot road") + " " +str("sector 3") +" " + str("121004")
    d['address'] = real_add
    geolocator = Nominatim(timeout=3)
    location = geolocator.geocode(pincode)

    lat = location.latitude
    lon = location.longitude
    d['lat'] = lat
    d['lon'] = lon
    l.append(d)
    print(l)
    return render(request,'map.html',{'l':l,'shape_detail':shape_detail})

@login_required
def shape(request):
    form = MapForm()
    if request.method=='POST':
        form=MapForm(request.POST, None)
        if form.is_valid():
            # print("a")
            form.save(commit=False)
            cmd = form.save(commit=False)
            cmd.user = request.user
            # print(cmd)
            cmd.save()
    return render(request,"shape_detail.html",{'form':form})
