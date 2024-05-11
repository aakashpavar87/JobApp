from django.shortcuts import redirect, render
from django.urls import reverse

from subscribe.forms import SubscribeForm
from subscribe.models import Subscribe

def thank_you(request):
    return render(request, 'subscribe/thankYou.html', context={})

# Create your views here.
def subscribe(request):
    subscribe_form = SubscribeForm()
    email_error_empty = ""
    if request.POST:
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        subscribe_form = SubscribeForm(request.POST)

        if subscribe_form.is_valid():
            print('Valid Form')
            cleaned_data = subscribe_form.cleaned_data
            print(cleaned_data)

            # Now you can access cleaned data for saving to the database
            Subscribe.objects.create(
                first_name=cleaned_data['first_name'],
                last_name=cleaned_data['last_name'],
                email=cleaned_data['email']
            )
            return redirect(reverse('thanks'))

    context = {'form': subscribe_form}
    return render(request, 'subscribe/subscribe.html', context)
