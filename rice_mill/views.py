from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from datetime import datetime

from . import models

# Create your views here.

@login_required
def landing(request):
   #return HttpResponse("Hello, world. You're at the polls index.")
   print( "is authenticated:", request.user.is_authenticated(), request.user.username)
   form_type = 1
   if request.method == 'POST':
       form_type = int(request.POST.get('formselector')[0].encode('utf-8'))
   title = { 1 : 'Purchase'
            ,2 : 'Sales' }.get(form_type)
   return render( request, 
           "rice_mill/index.html",
           context = { 'user': request.user
            ,'form_type': form_type
            ,'title': title
           } )

@login_required
def submit(request):
    #print ( request.POST.get('broker'), request.POST['rice_variety'] )
    print ( request.POST )
    
    purchases = models.purchase()
    user = request.user
    purchases.user = user
    purchases.date = datetime.now()

    broker_obj = models.broker( )
    broker_obj.broker_name = request.POST.get('broker').encode('utf-8')
    broker_obj.save()
    purchases.broker = broker_obj
    
    rice_variety_obj = models.rice_variety( )
    rice_variety_obj.rice_type = request.POST.get('rice_variety').encode('utf-8')
    rice_variety_obj.save()
    purchases._rice_variety = rice_variety_obj

    purchases.vehicle_no = request.POST.get('vehicle_no')

    bag_type_obj = models.bag_types()
    bag_type_obj.bag_type = int(request.POST.get('bag_type').encode('utf-8'))
    bag_type_obj.save()
    purchases.bag_type = bag_type_obj

    purchases.no_of_bags = int(request.POST.get('no_of_bags').encode('utf-8'))
    purchases.weighment = request.POST.get('weighment').encode('utf-8')

    print ( purchases.__str__() )
    purchases.save()

    return HttpResponse("<h1> Submitted SuccessFully</h1>")
