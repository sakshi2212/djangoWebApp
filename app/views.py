from django.shortcuts import render, redirect  
from app.forms import AbcForm  
from app.models import Abc  
# Create your views here.  
def create(request):  
    if request.method == "POST":  
        form = AbcForm(request.POST)  
        if form.is_valid(): 
            # obj = Abc.objects.all()
            # print(obj)
            # if(Abc.objects.filter(pk='id').exists()):
            #     print("true")
            # else:
            print(Abc.name) 
            try: 
               
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = AbcForm()  
    return render(request,'index.html',{'form':form})  
def show(request):  
    obj = Abc.objects.all()  
    return render(request,"show.html",{'obj':obj})  
