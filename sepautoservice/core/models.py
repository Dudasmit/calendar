from django.db import models
from django.conf import settings
from django.urls import reverse
from datetime import datetime, timedelta, date
# Create your models here.

class Winkel(models.Model):
    name = models.CharField(max_length=50)
    postcode = models.CharField(max_length=6,null=True) 
    adress = models.CharField(max_length=75)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        
        super(Winkel, self).save(*args, **kwargs)

class Apointments(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, 
                             #default=1,
                             on_delete=models.CASCADE,verbose_name="Gebruiker" )
    winkel = models.ForeignKey(Winkel,on_delete=models.CASCADE,verbose_name="Winkel")
    sity = models.CharField(max_length=50,verbose_name="Plaats")
    postcode = models.CharField(max_length=6) 
    
    shipping_address = models.CharField(max_length=100,verbose_name="Bezorgadres") 
    price = models.DecimalField( max_digits=10, decimal_places=2,null=True,verbose_name="Prijs")   
    start_time = models.DateTimeField(null=True,verbose_name="datum Tijd")
    
    client = models.CharField(max_length=100,verbose_name="Naam") 
    telefon = models.CharField(max_length=50,verbose_name="Telefoon")
    
    def __str__(self):
        return f'{self.winkel} - {self.sity} - {self.start_time}'
    
    def save(self, *args, **kwargs):
        
        super(Apointments, self).save(*args, **kwargs)
        
    def delete(self, *args, **kwargs):
        
        super(Apointments, self).delete(*args, **kwargs)
    
    @property
    def get_html_url(self):
        url = reverse('core:event_edit', args=(self.id,))
        delurl = reverse('core:delete', args=(self.id,))
        return f'<a href="{url}"> {self.winkel}- {self.sity}-{self.start_time.strftime("%x")} </a> <!--<a href="{delurl}"> "delete" </a>-->'
    
    def get_absolute_url(self):
        return reverse('core:event_edit', args=(self.id,))
    
    def get_delete_url(self):
        
        deleteurl = reverse('core:delete', args=(self.id,))
        return reverse('core:delete', args=(self.id,))
    
    def get_print_pdf_url(self,day, month, year,):
        
        return reverse('core:generate_pdf', args=(day, month, year,))
    
    def get_html_url_day(self, day, month, year):
        
        url = reverse('core:day', args=(day, month, year,))

        return f'<a href="{url}"> {day}</a>'
    