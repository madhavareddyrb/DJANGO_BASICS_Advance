from django.shortcuts import render
from django.http import HttpResponse
from django.views import *
# Create your views here.


def index(request):
  return render(request,"index.html")

def about(request):
  return render(request,"about.html")

def contact(request):
  return render(request,'contact.html')

def dynamic_url(request, id):
  print(f'This is the value that got in function --> {id}')
  return render(request,'dynamic_url.html',context={"id":id,'name':'madhava'})


class HomeView(View):
  template_name = 'classBaseView.html'

  def get(self,request):
    return render(request,self.template_name)
  def post(self,request):
    return render(request,self.template_name)
