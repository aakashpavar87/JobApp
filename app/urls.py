from django.http import HttpResponseNotFound
from django.urls import path
from app import views


# There are Four path converters
# 1. int
# 2. str
# 3. slug
# 4. uuid


def not_found(request, **kwargs):
    return HttpResponseNotFound("Not Found none Error Code : 404")

urlpatterns = [
    path('', views.hello, name='jobs_home'),
    # path('job/1', views.job_page) static url
    path('job/<int:id>', views.job_page, name='job_details'), # dynamic url than we have to accept that variable in our views.py
    path('job', views.job_info, name='jobs_info'), # dynamic url than we have to accept that variable in our views.py
    path('hello', views.hello_file, name='hello_file'),
    path('<path:invalid_path>', not_found),  # Catch-all pattern 
]
