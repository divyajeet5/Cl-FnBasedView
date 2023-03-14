from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django import forms
# Create your views here.

def homepage(request):
    return HttpResponse('<h1>Enter the desired url in the search bar</h1>' + '<h1>1) func</h1>' + '<h1>2) clas</h1>' + '<h1>3) fbvtemp</h1>' + '<h1>4) cbvtemp</h1>' + '<h1>5) cfunc</h1>' + '<h1>5.1) cclas</h1>')


class cbview(View):
    name = "Divyajeetsinh"
    def get(self, request):
        return HttpResponse('<h1>class based view</h1>' + self.name)


def fbview(request):
    return HttpResponse('<h1>Function based view</h1>')


def fbtemp(request):
    context = {'msg': 'Hello, welcome to function based view (Template Render)'}
    return render(request, 'Show/about.html', context)

class cbtemp(View):
    def get(self, request):
        return render(request, 'Show/about.html', {'msg': 'Hello, welcome to class based view (Template Render)'})


class ContactForm(forms.Form):
    name = forms.CharField(max_length=70)



def contactfunc(request):
    if request.method == 'POST':
        formobj = ContactForm(request.POST)
        if formobj.is_valid():
            print(formobj.cleaned_data['name'])
            return HttpResponse('Form has been submitted, Thank you!')
    else:
        formobj = ContactForm()
        return render(request, 'Show/contact.html', {'form': formobj})



class contactclas(View):

    def get(self, request):
        formobj = ContactForm()
        return render(request, 'Show/contact.html', {'form': formobj})

    def post(self, request):
        formobj = ContactForm(request.POST)
        if formobj.is_valid():
            print(formobj.cleaned_data['name'])
            return HttpResponse("Your form has been submitted")