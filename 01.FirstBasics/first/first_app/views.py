from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
  return HttpResponse ("Hi These is index page in these we are going to learn how to to send HttpResponse to client from server")
def about(request):
  return HttpResponse("Hi  These is about page")
def contact(request):
  return HttpResponse("hi These is contact page")