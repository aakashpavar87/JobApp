from django.db import models
from django.utils.text import slugify

# Create your models here.


# Model 
# Field
# Field Type
# Field Options

class Author(models.Model):
    name = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)

# creating relationships between more thsn one model
class Location(models.Model):
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    zip = models.CharField(max_length=200)


class JobPost(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    posted_date = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateField(null=True)
    salary = models.IntegerField()
    jobName = models.CharField(default="", max_length=100)
    slug = models.SlugField(null=True, unique=True, max_length=40)
    # This is for one-to-one relationship Ex: One JobPost related to One Location
    location = models.OneToOneField(Location, on_delete=models.CASCADE, null=True)
    # This is for many-to-one relationship Ex: Many JobPost related to one Author
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        """This method works as toString method of our model it overrides in built method of base class Model"""
        return f"{self.title} with salary of {self.salary}"
    
    def save(self,*args,**kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        return super(JobPost,self).save(*args, **kwargs)