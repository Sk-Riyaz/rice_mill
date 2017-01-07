from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models

from common_settings import *
# Create your models here.

class broker(models.Model):
    broker_name = models.TextField(max_length=MAX_NAME_LENGTH, 
            unique=False, default='unknown')

    def __str__(self):
        return self.broker_name

class rice_variety(models.Model):
    rice_type = models.CharField(max_length=MAX_GEN_LENGTH_100, 
            unique=False)

    def __str__(self):
        return self.rice_type

class bag_types(models.Model):
    bag_type = models.IntegerField(unique=False)

    def __str__(self):
        bag_type_dict = { 50: "Small"
                         ,100: "Big"
                        }
        return bag_type_dict.get( self.bag_type )

class purchase(models.Model):
    user = models.ForeignKey(User)
    date = models.DateTimeField(auto_now_add=True)
    broker = models.ForeignKey(broker, on_delete=models.PROTECT)
    _rice_variety = models.ForeignKey(rice_variety, on_delete=models.PROTECT)
    vehicle_no = models.CharField(max_length=MAX_GEN_LENGTH_100)
    bag_type = models.ForeignKey(bag_types)
    no_of_bags = models.IntegerField()
    weighment = models.IntegerField()

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return (self.user, str(self.date), self.broker.__str__(),
                self._rice_variety.__str__(), self.vehicle_no, 
                self.bag_type.__str__(), self.no_of_bags, self.weighment).__str__()
        #return (self.user, str(self.date), self.broker, 
        #        self._rice_variety, self.vehicle_no, self.bag_type, 
        #        self.no_of_bags, self.weighment).__str__()

    def get_purchases(self):
        return purchase.objects.filter(parent=self).order_by('date')

