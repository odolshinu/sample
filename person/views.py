import datetime

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse

from .models import Blog, Pizza, Person
from .forms import PersonForm, PersonModelForm

# Create your views here.

def home(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def blog(request):
    #return HttpResponseNotFound('<h1>Page not found</h1>')
    return HttpResponseRedirect(reverse('pizza'))


def pizza(request):
    pizzas = Pizza.objects.all()
    return render_to_response('pizza.html', {'pizzas':pizzas})

def pizza_details(request, id):
    if request.method == 'POST':
        person_form = PersonModelForm(request.POST)
        print person_form
        if person_form.is_valid():
            print "form is valid"
            person_form.save()
        else:
            print "error"
            return HttpResponse("Error")
        #p = Person()
        #p.first_name = request.POST['first_name']
        #p.last_name = request.POST['last_name']
        #p.age = request.POST['age']
        #p.save()
    pizza = Pizza.objects.get(id=id)
    persons = Person.objects.all()
    person_form = PersonForm()
    return render(request, 'pizza_detail.html', {'pizza':pizza, 'persons':persons, 'form':person_form, 'test':[1,2,3]})











