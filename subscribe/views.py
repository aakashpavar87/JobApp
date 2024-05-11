from django.shortcuts import render

from subscribe.forms import SubscribeForm
from subscribe.models import Subscribe

# Create your views here.
def subscribe(request):
    subscribe_form = SubscribeForm()
    email_error_empty = ""
    if request.POST:
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid:
            print(subscribe_form.cleaned_data)
        # Subscribe.objects.create(first_name=first_name, last_name=last_name, email=email)
    
    context = {'form': subscribe_form}
    return render(request, 'subscribe/subscribe.html', context)