from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.urls import reverse
from django.template import loader

from app.models import JobPost
# from django.urls import reverse

job_title = [
    "First Title",
    "Second Title",
    "Third title"
]

jobs = [
    "Python Developer",
    "PHP Developer",
    "JAVA Developer"
]

job_description = [
    "First Description",
    "Second Description",
    "Third Description"
]

# Create your views here.
def hello(request):
    try:
        html_res = "<ul>"
        for job in jobs:
            job_id = jobs.index(job) + 1
            print(reverse('job_details', args=(job_id,)))
            html_res+= f"""
                        <li> <a href="{reverse('job_details', args=(job_id,))}">{job}</a> </li>
                    """
        html_res += f"</ul><br /><a href='{reverse('jobs_info')}'>Info</a>"
        return HttpResponse(html_res)
    except:
        return HttpResponseNotFound("Not Found Hello !!! 404")


def hello_file(request):
    newJobs = JobPost.objects.filter()
    context = {'name': 'Aakash', 'jobs':newJobs, 'desc':job_description}
    return render(request, 'home/hello.html', context)

# New Function that interact with database
def job_page(request, id):
    try:
        print(id)
        foundJob = JobPost.objects.filter(slug=id)[0]
        context = {
            'job_title': foundJob.title,
            'job_description': foundJob.description,
            'job_salary': foundJob.salary,
            'job': foundJob
        }
        return render(request,'home/job_detail.html', context)
    except:
        return HttpResponseNotFound("Not Found any ID !!! 404")


# def job_page(request, id):
#     try:
#         site = "localhost:8080"
#         redirect_id = id - 1
#         print(type(id))
#         if redirect_id == 0:
#             return redirect("/")
#         context = {
#             'job_title': jobs[redirect_id],
#             'job_description': job_description[redirect_id]
#         }
#         return render(request,'home/job_detail.html', context)
#     except:
#         return HttpResponseNotFound("Not Found any ID !!! 404")

def job_info(request):
    try:
        site = "localhost:8080"
        html_response = f"""<h1>Nothing Special</h1><br />
                            <h3> <a href={reverse('jobs_home')}>Home</a> </h3>
                         """
        return HttpResponse(html_response)
    except:
        return HttpResponseNotFound("Not Found any Page !!! 404")



# html_response = f"""<h1>{job_title[int(id) - 1]}</h1><br/>
#                     <h4>{job_description[int(id) - 1]}</h4>"""
# return HttpResponse(f"""<h4>Job Page Job Id  : {id}</h4>
#                     <a href={site}>Click Here</a>
#                     """)