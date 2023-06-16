from email import message
from django.shortcuts import redirect, render, HttpResponse
from .models import Notes, Homework, Todo
from django.contrib import messages
import random
from package import youtube_module
from package import wiki_module

def home(request):
    return render(request, 'home.html')

def notes(request):
    if request.method=='POST':
        title = request.POST['title']
        description = request.POST['description']

        new_note = Notes(title=title, description=description)
        new_note.save()
        messages.success(request, "Note Successfully Added")
        return redirect("notes")
    note = Notes.objects.all()   

    return render(request, 'notes.html', {'note':note})

def note_details(request, nid):
    note = Notes.objects.get(id = nid) 
    return render(request, 'note_details.html', {'note':note})

def note_delete(request, did=0):
    remove_note = Notes.objects.get(id=did)
    remove_note.delete()
    messages.success(request, 'Note Successfully deleated')
    return redirect("notes")

def homework(request):
    homework = Homework.objects.all()  
    if request.method=='POST':
        title = request.POST['title']

        try:
            status = request.POST['status']
            if status =='on':
                status = True
            else:
                status = False
        except:
            status = False
            
        new_homework = Homework(title=title, status=status)
        new_homework.save()
        messages.success(request, "Homework Successfully Added")
        return redirect("homework")
    return render(request, 'homework.html', {'homework':homework})

def homework_delete(request, did=0):
    remove_homework = Homework.objects.get(id=did)
    remove_homework.delete()
    messages.success(request, 'Homework Successfully deleated')
    return redirect("homework")

def youtube(request):
    if request.method == 'POST':
        search = request.POST['search']
        result = youtube_module.youtube_search(search)
        
        return render(request, 'youtube.html', {'result':result})
    return render(request, 'youtube.html')

def todo(request):
    todos = Todo.objects.all()  
    if request.method=='POST':
        title = request.POST['todotitle']

        try:
            todostatus = request.POST['todostatus']
            if todostatus =='on':
                todostatus = True
            else:
                todostatus = False
        except:
            todostatus = False
        print(todostatus)
        new_todo = Todo(title=title, todostatus=todostatus)
        new_todo.save()
        messages.success(request, "TODO Successfully Added")
        return redirect("todo")
    return render(request, 'todo.html', {'todos':todos})

def todo_delete(request, did=0):
    remove_todo = Todo.objects.get(id=did)
    remove_todo.delete()
    messages.success(request, 'TODO Successfully deleated')
    return redirect("todo")

def wiki(request):
    if request.method == 'POST':
        wiki = request.POST['wiki']
        result = wiki_module.wiki_search(wiki)
        
        return render(request, 'wiki.html', {'result':result})
    return render(request, 'wiki.html')