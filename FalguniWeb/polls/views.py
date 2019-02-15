from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import User, Poll_admin
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    template = loader.get_template('polls/index.html')
    return HttpResponse(template.render())

@csrf_exempt
def login(request):
    if request.method != "POST":
        return HttpResponse("you're lost bro")
    email = request.POST.get('email')
    password = request.POST.get('password')
    qset = User.objects.filter(email=email)
    
    for q in qset:
        if q.password == password:
            request.session['user'] = email
            return redirect('/polls/homepage')
    return render(request, 'polls/index.html', {})

@csrf_exempt
def signup(request):
    if request.method != "POST":
        return HttpResponse("you're lost bro")
    if request.POST.get('email') == "" or request.POST.get('password') == "":
        return render(request, 'polls/index.html', {'error': "error : email/password empty"})

    email = request.POST.get('email')
    username = request.POST.get('username')
    password = request.POST.get('password')

    qset = User.objects.all()
    

    for q in qset:
        print("q  ------------ ", q.email)
        if q.email == email:
            return render(request, 'polls/index.html', {'error': "error : user with this email already exists"})


    new_user = User(full_name=username, email=email, password=password)
    new_user.save()
    return redirect('/polls/index')


@csrf_exempt
def homepage(request):
    if 'user' not in request.session or request.session['user'] == -1:
        return render(request, 'polls/index.html', {})
    qset = User.objects.all()
    lst = []
    for q in qset:
        lst.append(q.email)
    
    template = loader.get_template('polls/homepage.html')

    return HttpResponse(template.render(context={'user': request.session['user'], 'lst': lst}))


@csrf_exempt
def nominate(request):
    if 'user' not in request.session or request.session['user'] == -1:
        return render(request, 'polls/index.html', {})
    
    qset = User.objects.all()

    for q in qset:
        if q.email==request.POST.get('nomination'):
            q.is_nominated = True
            q.save()
            break
    
    return redirect('/polls/homepage')


@csrf_exempt
def votepage(request):
    if 'user' not in request.session or request.session['user'] == -1:
        return render(request, 'polls/index.html', {})
    qset = User.objects.filter(is_nominated=True)
    lst = []
    for q in qset:
        lst.append(q.email)
    
    template = loader.get_template('polls/votepage.html')

    return HttpResponse(template.render(context={'user': request.session['user'], 'lst': lst}))


