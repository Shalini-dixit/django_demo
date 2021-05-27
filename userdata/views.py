from django.shortcuts import render
from userdata.models import User
# Create your views here.

def index(request):
    #return HttpResponse("<em>My Second App </em>")
    my_dict = {"insert_me": "In the view.py right now"}
    return render(request,'userdata/index.html',context=my_dict)

def user(request):
    data = User.objects.all()
    context = {'data': data}
    return render(request, 'userdata/user.html', context)
    