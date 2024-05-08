(env) PS C:\Users\Aakash Pavar\Desktop\Django\JobApp> python manage.py makemmigrations
Unknown command: 'makemmigrations'. Did you mean makemigrations?
Type 'manage.py help' for usage.
(env) PS C:\Users\Aakash Pavar\Desktop\Django\JobApp> python manage.py makemigrations
Migrations for 'app':
app\migrations\0007_author_jobpost_author.py - Create model Author - Add field author to jobpost
(env) PS C:\Users\Aakash Pavar\Desktop\Django\JobApp> python manage.py migrate
Operations to perform:
Apply all migrations: admin, app, auth, contenttypes, sessions
Running migrations:
Applying app.0007_author_jobpost_author... OK
(env) PS C:\Users\Aakash Pavar\Desktop\Django\JobApp> python manage.py shell
Python 3.12.3 (tags/v3.12.3:f6650f9, Apr 9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)

> > > from app.models import JobPost,Location,Author
> > > author_1=Author(name="Jimmy Carter", company="GOOGLE", designation="HR")
> > > author_1.save()
> > > author_2=Author(name="Stacy Gold Burg", company="Face Book", designation="HR")
> > > author_2.save()
> > > ninth_job = JobPost(title="Ninth Job Post", description="Demo Ninth Job", salary=12000)  
> > > ninth_job.save()
> > > ninth_job.author = author_1
> > > ninth_job.save()
> > > sixth_job=JobPost.objects.get(title**contains="sixth")
> > > sixth_job.author= author_2
> > > sixth_job.save()  
> > > author_3=Author(name="Michel Smith", company="Netflix", designation="HR")  
> > > author_3.save()
> > > fifth_job= JobPost.objects.get(title**icontains="fifth")
> > > fifth_job
> > > <JobPost: Fifth Job with salary of 1200>
> > > fifth_job.author=author_3
> > > fifth_job.save()
> > > node_job= JobPost.objects.get(title**icontains="node")  
> > > node_job.author = author_1  
> > > node_job.save()
> > > author_1.jobpost_set.all()
> > > <QuerySet [<JobPost: Node Js Developer with salary of 25000>, <JobPost: Ninth Job Post with salary of 12000>]>
> > > Author.objects.get(name**icontains="jimmy").jobpost_set.all()
> > > <QuerySet [<JobPost: Node Js Developer with salary of 25000>, <JobPost: Ninth Job Post with salary of 12000>]>
> > > new_job_author= author_2.jobpost_set.create(title="Tenth Job", description="Tenth Job by Author", salary=13000)
> > > author_2.jobpost_set.all()
> > > <QuerySet [<JobPost: sixth job post with salary of 23000>, <JobPost: Tenth Job with salary of 13000>]>
> > > author_2
> > > <Author: Author object (2)>
> > > author_2.name
> > > 'Stacy Gold Burg'
> > > author_2.jobpost_set.add(JobPost.objects.get(title**icontains="django"))
> > > author_2.jobpost_set.add(JobPost.objects.get(title**icontains="spring"))
> > > JobPost.objects.get(title**icontains="django").author.name
> > > 'Stacy Gold Burg'
> > > JobPost.objects.get(title**icontains="spring").author.name
> > > 'Stacy Gold Burg'
> > > 'Stacy Gold Burg'
> > > 'Stacy Gold Burg'
> > > author_2.jobpost_set
> > > <django.db.models.fields.related_descriptors.create_reverse_many_to_one_manager.<locals>.RelatedManager object at 0x0000023DC1AB5880>
> > > author_2.jobpost_set.all()
> > > <QuerySet [<JobPost: Django Rest Developer with salary of 5000>, <JobPost: Spring boot java developer with salary of 3000>, <JobPost: sixth job post with salary of 23000>, <JobPost: Tenth Job with salary of 13000>]>
> > > author_2.jobpost_set.all().count
> > > <bound method QuerySet.count of <QuerySet [<JobPost: Django Rest Developer with salary of 5000>, <JobPost: Spring boot java developer with salary of 3000>, <JobPost: sixth job post with salary of 23000>, <JobPost: Tenth Job with salary of 13000>]>>
> > > author_2.jobpost_set.all().count()
> > > 4
> > > JobPost.objects.filter(author**name="Stacy")
> > > <QuerySet []>
> > > JobPost.objects.filter(author**name**icontains="Stacy")
> > > <QuerySet [<JobPost: Django Rest Developer with salary of 5000>, <JobPost: Spring boot java developer with salary of 3000>, <JobPost: sixth job post with salary of 23000>, <JobPost: Tenth Job with salary of 13000>]>
> > > JobPost.objects.filter(author**name**icontains="Stacy").count()
> > > 4
> > > JobPost.objects.filter(author**name**icontains="Jimmy").count()
> > > 2
> > > JobPost.objects.filter(author**name**icontains="jimmy")
> > > <QuerySet [<JobPost: Node Js Developer with salary of 25000>, <JobPost: Ninth Job Post with salary of 12000>]>
> > > JobPost.objects.filter(author**company**icontains="google")
> > > <QuerySet [<JobPost: Node Js Developer with salary of 25000>, <JobPost: Ninth Job Post with salary of 12000>]>
> > > JobPost.objects.filter(author**company**icontains="facebook")
> > > <QuerySet []>
> > > JobPost.objects.filter(author**company**icontains="face")  
> > > <QuerySet [<JobPost: Django Rest Developer with salary of 5000>, <JobPost: Spring boot java developer with salary of 3000>, <JobPost: sixth job post with salary of 23000>, <JobPost: Tenth Job with salary of 13000>]>
> > > JobPost.objects.filter(author**company**icontains="face").count()
> > > 4
> > > JobPost.objects.filter(author**company**icontains="face").count()
> > > 4
> > > JobPost.objects.filter(author**in=[1,2])  
> > > <QuerySet [<JobPost: Node Js Developer with salary of 25000>, <JobPost: Ninth Job Post with salary of 12000>, <JobPost: Django Rest Developer with salary of 5000>, <JobPost: Spring boot java developer with salary of 3000>, <JobPost: sixth job post with salary of 23000>, <JobPost: Tenth Job with salary of 13000>]>
> > > JobPost.objects.filter(author**in=[1,3])
> > > <QuerySet [<JobPost: Node Js Developer with salary of 25000>, <JobPost: Ninth Job Post with salary of 12000>, <JobPost: Fifth Job with salary of 1200>]>
> > > JobPost.objects.filter(author**in=[1,3]).count()
> > > 3
> > > JobPost.objects.filter(author**pk=1)  
> > > <QuerySet [<JobPost: Node Js Developer with salary of 25000>, <JobPost: Ninth Job Post with salary of 12000>]>
> > > JobPost.objects.filter(author**pk=2)
> > > <QuerySet [<JobPost: Django Rest Developer with salary of 5000>, <JobPost: Spring boot java developer with salary of 3000>, <JobPost: sixth job post with salary of 23000>, <JobPost: Tenth Job with salary of 13000>]>
> > > JobPost.objects.filter(author**pk=3)
> > > <QuerySet [<JobPost: Fifth Job with salary of 1200>]>
> > > Author.objects.filter(jobpost=1)  
> > > <QuerySet [<Author: Author object (2)>]>
> > > Author.objects.filter(jobpost=3)
> > > <QuerySet []>
> > > Author.objects.filter(jobpost**title**icontains="fifth")
> > > <QuerySet [<Author: Author object (3)>]>
> > > Author.objects.get(jobpost**title**icontains="fifth").name  
> > > 'Michel Smith'
> > > Author.objects.get(jobpost**title\_\_icontains="fiftbbvbh").name
