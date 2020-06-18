from django.shortcuts import render

# Create your views here.
# my import
from.models import cpt
from .models import Create
from django import forms
from django.http import HttpResponse
from .form import ApplyCreate

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
### app def
@login_required(login_url="/login/")
def index(request):
    return render(request, "index.html")

@login_required(login_url="/login/")
def pages(request):
    context = {}

    
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template = request.path.split('/')[-1]
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'error-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'error-500.html' )
        return HttpResponse(html_template.render(context, request))
# my def 

def create(request):
    create = Create.objects.all()
    if request.method=='POST':
       form = Create(request.POST)
       if form.is_valid():
           form = form.save()
    else :
        form = ApplyCreate()
    context = {'create' : create , 'form':form}
    return render (request,'cpt.html',context)
 

# # def index(request):

#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)




# def create(request):
#     pass
# print("=======")



