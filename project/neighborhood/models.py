from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from PIL import Image
from django_countries.fields import CountryField


# Create your models here.

class Neighborhood(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    occupants_count = models.IntegerField()
    pub_date = models.DateTimeField(auto_now_add=True)
    Admin = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    country = CountryField(blank_label='(select country)', default='NG')

        
    def save_neighborhood(self):
        self.save()
    
    def delete_neighborhood(self):
        self.delete()
        
    @classmethod
    def get_neighborhoods(cls):
        projects = cls.objects.all()
        return projects
    
    @classmethod
    def search_neighborhoods(cls, search_term):
        projects = cls.objects.filter(name__icontains=search_term)
        return projects
    
    
    @classmethod
    def get_by_admin(cls, Admin):
        projects = cls.objects.filter(Admin=Admin)
        return projects
    
    
    @classmethod
    def get_neighborhood(request, neighborhood):
        try:
            project = Neighborhood.objects.get(pk = id)
            
        except ObjectDoesNotExist:
            raise Http404()
        
        return project
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'My Neighborhood'
        verbose_name_plural = 'Neighborhoods'
