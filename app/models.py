from django.db import models
from django.utils.text import slugify

# Create your models here.


# Model 
# Field
# Field Type
# Field Options

class JobPost(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    posted_date = models.DateTimeField(auto_now_add=True)
    salary = models.IntegerField()
    jobName = models.CharField(default="", max_length=100)
    slug = models.SlugField(null=True, unique=True, max_length=40)
    
    def save(self,*args,**kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        return super(JobPost,self).save(*args, **kwargs)
    
    # This method works as toString method of our model it overrides in built method of base class Model
    def __str__(self):
        return self.title
    