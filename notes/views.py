from email import message
from django.shortcuts import redirect, render, HttpResponse
from .models import Notes, Homework, Todo
from django.contrib import messages
from youtubesearchpython import VideosSearch
import wikipedia
import random

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
        video = VideosSearch(search, limit=10)
        result = []
        for i in video.result()['result']:
            resultdict = {
                'input':search,
                'title' : i['title'],
                'duration' : i['duration'],
                'thumbnails' : i['thumbnails'][0]['url'],
                'channel' : i['channel']['name'],
                'link' : i['link'],
                'viewcount' : i['viewCount']['short'],
                'published' : i['publishedTime'],
            }
            result.append(resultdict)
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
        

        try:
            p = wikipedia.page(wiki, auto_suggest=False)
        except wikipedia.DisambiguationError as e:
            s = random.choice(e.options)
            p = wikipedia.page(s)

        
        result = []
        details = {
            'input' : p,
            'title' : p.title,
            'link'  : p.url,
            'details' : p.summary,
        }
        result.append(details)
        return render(request, 'wiki.html', {'result':result})
    return render(request, 'wiki.html')