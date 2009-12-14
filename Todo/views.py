# Create your views here.

from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from GTD.Todo.models import Todo,User


"""
__author__:"Aravind Muthu"
__email__:"aravind.geek@gmail.com"
"""
def todoform(request):
    name=request.session['user_id']
    return render_to_response('todolist.html',{"user":name})


def entry_todo(request):
    """
    Entry the subject,date,priority values into DB
    """
    errors=[]
    if request.method=='POST':
        if (not request.POST['subject'])or (not request.POST['date'])or (not request.POST['priority']):                        
            errors.append("Pls Fill all details") 
            return render_to_response("todolist.html",{'error':errors,'user':request.session['user_id']})
        else:
            try:
                post=Todo(user_id=request.session['user_id'],subject=request.POST['subject'],date=request.POST['date'],priority=request.POST['priority']) #post values into DB
                post.save()   #commit save
            except:
               
                return render_to_response("todolist.html",{"error":''})
    return render_to_response("todolist.html",{"noerror":'Successfully saved',"user":request.session['user_id']})


def show_todo(request):
    """
    Fetching To-do list data from DB
    
    """
    #username=Todo.objects.filter('user')
    #name=request.GET['user']
    name=request.session['user_id']
    entry=Todo.objects.filter(user_id=name)    #Fetch data from DB using user_id
    return render_to_response("show.html",{'entrys':entry ,"user":name})
    
def entry_delete(request):
    """ Delete all the item from db by session user_id """
    name=request.session['user_id']
    entry=Todo.objects.filter(user_id=name).delete()#To delete
    return render_to_response('show.html',{"entrys":entry})
    
   # return render_to_response("show.html")


def create_user(request):

    """ To create an GTD user account """
    errors=[]
    if request.method=="POST":
        if(not request.POST['username'])or (not request.POST['password']):
           # errors.append("pls enter all details")
            return render_to_response('signup.html',{'error':'pls enter all details'})
        else:
            
            try:
                username=request.POST['username']
                if User.objects.filter(user=username):
                    
                    errors.append("Username already exits ")
                    return render_to_response("signup.html",{"erro":errors})
                else:
                    
                    post=User(user=request.POST['username'],password=request.POST['password'])
                    post.save()
                    
            except:
             
                return render_to_response('signup.html',{'error':" User ID already exist!"})

    return render_to_response('signup.html',{"info":"Successfully created"})

def login(request):
    """ It gives access to the existing user to access GTD  """
    if request.method=="POST":
       if (request.POST['username'] and request.POST['password']) :
          try:
            username=request.POST['username']
            password=request.POST['password']
            user=User.objects.get(user=username,password=password)
            request.session['user_id']=username
            return render_to_response("todolist.html",{'user':username})
          except:
            return render_to_response("login.html",{"error":"Incorrect username or password!"})
       else:
           return render_to_response("login.html",{"error":"Provide username or password!"})
    else:
        return render_to_response("login.html")#,{"error":"Provide username or password!"})

def signup(requset):
    """ Which gives the registration form """
    return render_to_response("signup.html")

def logout(request):
    """ exit from GTD"""
    request.session.clear()
    return HttpResponseRedirect('/GTD/')

def show(request,id):
    name=request.session['user_id']
    
    if Todo.objects.filter(user_id=name,item_id=id):
        
        entry=Todo.objects.filter(item_id=id)
        
        return render_to_response('update.html',{"entrys":entry,"user":name})
    else:
        return HttpResponse('No page Found')

def update(request,id):
    """ To update the Pending item """
    
    errors=[]
    if request.method=='POST':
        if (not request.POST['subject'])or (not request.POST['date'])or (not request.POST['priority']):                        
            errors.append("Pls Fill all details") 
           
            entry=Todo.objects.filter(item_id=id)
            return render_to_response("update.html",{'error':errors,'user':request.session['user_id'],'entrys':entry})
        else:
            try:
                post=Todo.objects.filter(item_id=id).update(user_id=request.session['user_id'],subject=request.POST['subject'],date=request.POST['date'],priority=request.POST['priority']) #append the values into DB
                
            except:
                entry=Todo.objects.filter(item_id=id)
                errors.append("Enter proper date")
                return render_to_response("update.html",{"error":errors,"entrys":entry})
            
            name=request.session['user_id']
            entry=Todo.objects.filter(item_id=id)
                 
    return render_to_response("update.html",{'info':'Successfully updated','user':request.session['user_id'],'entrys':entry})
   
    
    




def debuginfo(request):
    request.session.clear()
    return render_to_response('404.html')


def delete_item(request,id):
    """ It does delete the item which is selected by user """
    name=request.session['user_id']
    delet=Todo.objects.filter(user_id=name,item_id=id).delete()
    return HttpResponseRedirect('/getfromdb/')

