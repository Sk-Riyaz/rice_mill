from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from . import models

# Create your views here.

#@login_required
def landing(request):
   #return HttpResponse("Hello, world. You're at the polls index.")
   print( "is authenticated:", request.user.is_authenticated(), request.user.username)
   form_type = 1
   if request.method == 'POST':
       form_type = int(request.POST.get('formselector')[0].encode('utf-8'))
   return render( request, 
           "rice_mill/index.html",
           context = { 'user': request.user
            ,'form_type': form_type
           } )

#@login_required
def submit(request):
    #print ( request.POST.get('broker'), request.POST['rice_variety'] )
    print ( request.POST )

    return HttpResponse("<h1> Submitted SuccessFully</h1>")
