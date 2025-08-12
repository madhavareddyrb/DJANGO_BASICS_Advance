from django.shortcuts import render

# Create your views here.

def index(request):
  import random
  lucky_number = random.randint(100,999)
  person_age = 2
  vegtables = ['tomato 🍅','carrot 🥕', 'califlower 🥙']
  student_data = [
    {'name':'madhava','age':22,'Study':'Completed'},
    {'name':'ram','age':26,'Study':'Completed'},
    {'name':'vinay','age':16,'Study':'Not Completed'},
    {'name':'yogi','age':15,'Study':'Not Completed'},
  ]
  for veg in vegtables:
    print(veg)
  context = {'lucky_number':lucky_number,'vegtables':vegtables,'person_age':person_age,'student_data':student_data}
  return render(request,'index.html',context)


