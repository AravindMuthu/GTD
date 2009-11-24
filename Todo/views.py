# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render_to_response
from DjangoTodo.Todo.models import Todo
"""
      My Todo Controller
      _author_:Aravind
      _email_:aravind.geek@gmail.com

"""
def todoform(request):
    return render_to_response('todolist.html')


def entry_todo(request):
    """
    DB-->DataBase
    Entry the subject,date,priority values into DB
    """
    errors=[]
    if request.method=='POST':
        if (not request.POST['subject'])or (not request.POST['date'])or (not request.POST['priority']):                        
            errors.append("Pls Fill all details")
            return render_to_response("todolist.html",{'error':errors})
        else:
            try:
                post=Todo(subject=request.POST['subject'],date=request.POST['date'],priority=request.POST['priority']) #post values into DB
                post.save()   #commit save
            except:
                return render_to_response("todolist.html",{"error":['Enter proper date YYYY-MM-DD']})
    return render_to_response("todolist.html",{"error":['Successfully saved']})


def show_todo(request):
    """
    show the Todo list from DB
    """
    entry=Todo.objects.all().order_by("-date")    #show Todo list by reverse order date
    return render_to_response("show.html",{'entrys':entry})

def entry_delete(request):
    
    entry=Todo.objects.all().delete()
    return render_to_response('show.html',{"entrys":entry})
    
   # return render_to_response("show.html")
