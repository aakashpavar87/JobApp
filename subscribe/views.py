from django.shortcuts import redirect, render
from django.urls import reverse

from subscribe.forms import SubscribeForm
from subscribe.models import Subscribe

def thank_you(request):
    return render(request, 'subscribe/thankYou.html', context={})

# Create your views here.
def subscribe(request):
    subscribe_form = SubscribeForm()
    if request.POST:
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form.save()
                        
            return redirect(reverse('thanks'))

    context = {'form': subscribe_form}
    return render(request, 'subscribe/subscribe.html', context)


# Old Code For saving in db
# print('Valid Form')
# cleaned_data = subscribe_form.cleaned_data
# print(cleaned_data)

# # Now you can access cleaned data for saving to the database
# Subscribe.objects.create(
#     first_name=cleaned_data['first_name'],
#     last_name=cleaned_data['last_name'],
#     email=cleaned_data['email']
# )
