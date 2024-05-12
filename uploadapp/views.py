from django.shortcuts import render

from uploadapp.forms import UploadFileForm, UploadForm

# Create your views here.
def upload_image(request):
    if request.POST:
        upload_form = UploadForm(request.POST, request.FILES)
        if upload_form.is_valid():
            print('In valid method')
            upload_form.save()
            saved_image = upload_form.instance
            context = {
                'form':upload_form,
                'saved_image': saved_image
            }
            return render(request, 'uploadapp/upload.html', context=context)
    else:
        upload_form = UploadForm()
    return render(request, 'uploadapp/upload.html', context={'form':upload_form})

def upload_file(request):
    if request.POST:
        upload_form = UploadFileForm(request.POST, request.FILES)
        if upload_form.is_valid():
            print('In valid method')
            upload_form.save()
            saved_file = upload_form.instance
            context = {
                'form':upload_form,
                'saved_file': saved_file
            }
            return render(request, 'uploadapp/upload-file.html', context=context)
    else:
        upload_form = UploadFileForm()
    return render(request, 'uploadapp/upload-file.html', context={'form':upload_form})