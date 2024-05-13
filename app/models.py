from django.db import models
from django.utils.text import slugify

# Create your models here.


# Model 
# Field
# Field Type
# Field Options


class Skills(models.Model):
    """Skills

    Args:
        models (Skills): Skills for job profile

    Returns:
        str: Skills required for JobPost
    """
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Author(models.Model):
    """Auhtor of JobPost

    Args:
        models (Author): JobPost Auhtor
    """
    name = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

# creating relationships between more thsn one model
class Location(models.Model):
    """Location of Job Post

    Args:
        models (): JobPost

    Returns:
        str: "Location"
    """
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    zip = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.street}, {self.city}"


class JobPost(models.Model):
    JOB_TYPE_CHOICES = [
        ('FULL', 'Full Time'),
        ('PART', 'Part Time'),
        ('INTERN', 'Intern Ship')
    ]
    
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
    # This is for many-to-many realtionship Ex: One JobPost have many Skills and Vice Versa
    skills = models.ManyToManyField(Skills)
    type= models.CharField(max_length=100, default='FULL', null=False, choices=JOB_TYPE_CHOICES)
    
    def __str__(self):
        """This method works as toString method of our model it overrides in built method of base class Model"""
        return f"{self.title} with salary of {self.salary}"
    
    def save(self,*args,**kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        return super(JobPost,self).save(*args, **kwargs)