from django.shortcuts import render, redirect  
from app.forms import MovieForm  
from app.models import Movie  
# Create your views here.  
def create(request):  
    if request.method == "POST":  
        form = MovieForm(request.POST)  
        if form.is_valid(): 
            # obj = Movie.objects.all()
            # print(obj)
            # if(Movie.objects.filter(pk='id').exists()):
            #     print("true")
            # else:
            print(Movie.name) 
            try: 
               
                form.save()
                   
                return redirect('/show')
                
            except:  
                pass 
        form = MovieForm() 
    else:  
        form = MovieForm()  
    return render(request,'index.html',{'form':form})  
def show(request):  
    obj = Movie.objects.all()  
    return render(request,"show.html",{'obj':obj})  
