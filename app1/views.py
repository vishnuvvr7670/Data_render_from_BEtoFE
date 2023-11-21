from django.shortcuts import render
data='This data is a Assumption'
name='Vishnu'
age=21
d={'assumption':data,'username':name,'age':21}

# Create your views here.
def data_render(request):
    return render(request,'data_render.html',context=d)
def login(request):
    return render(request,'data_render.html',context=d)