from django.contrib import admin

from django.contrib.admin import AdminSite

#from .models import MyModel

# Register your models here.

class MyAdminSite(AdminSite):
   site_header = 'RiceMill Administration'
   site_title = "Admin Login"
   site_url = None
   #login_template = "admin/rice_mill/login.html"

admin_site = MyAdminSite(name='myadmin')
admin.autodiscover()
#admin_site.register(MyModel)
