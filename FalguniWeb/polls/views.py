from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import User, Poll_admin, PM, Mayor, Councillor
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
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
    who = -1
    for q in qset:
        if q.password == password:
            request.session['user'] = email
            who = email
            break
    if who == -1:
        return render(request, 'polls/index.html', {})
    
    is_election_set = Poll_admin.objects.all()[0].is_time_set
    if is_election_set == True:
        start_time = Poll_admin.objects.all()[0].start_time
        end_time = Poll_admin.objects.all()[0].end_time
        now = timezone.now()
        print("_________", now, "______", start_time)
        if now > start_time and now < end_time:
            return redirect('/polls/votepage')
        elif now > end_time:
            return redirect('/polls/', context={'error': "Sorry election time is over"})

    return redirect('/polls/homepage')


@csrf_exempt
def signup(request):
    if request.method != "POST":
        return HttpResponse("you're lost bro")
    if request.POST.get('email') == "" or request.POST.get('password') == "":
        return render(request, 'polls/index.html', {'error': "Email or Password is empty"})

    email = request.POST.get('email')
    username = request.POST.get('username')
    password = request.POST.get('password')

    qset = User.objects.all()
    

    for q in qset:
        print("q  ------------ ", q.email)
        if q.email == email:
            return render(request, 'polls/index.html', {'error': "User with this email already exists"})


    new_user = User(full_name=username, email=email, password=password)
    new_user.save()
    return render(request, 'polls/index.html', {'message': "Registration successful. You can now login"})



@csrf_exempt
def homepage(request):
    if 'user' not in request.session or request.session['user'] == -1:
        return render(request, 'polls/index.html', {'error': "error : user logged out"})


    qset = User.objects.all()
    lst = []
    status = []
    for q in qset:
        if q.email != request.session['user']:    
            lst.append(q.email)

    template = loader.get_template('polls/homepage.html')

    return HttpResponse(template.render(context={'user': request.session['user'], 'lst': lst}))



@csrf_exempt
def nominate(request):
    if 'user' not in request.session or request.session['user'] == -1:
        return render(request, 'polls/index.html', {})
    
    qset = User.objects.all()

    for q in qset:
        if q.email==request.POST.get('nomination_PM'):
            q.is_nominated_PM = True
            q.save()
            break
        if q.email==request.POST.get('nomination_mayor'):
            q.is_nominated_mayor = True
            q.save()
            break
        if q.email==request.POST.get('nomination_councillor'):
            q.is_nominated_councillor = True
            q.save()
            break
    
    return redirect('/polls/homepage')


@csrf_exempt
def votepage(request):
    if 'user' not in request.session or request.session['user'] == -1:
        return render(request, 'polls/index.html', {})
    
    qset = User.objects.filter(email=request.session['user'])
    q = qset[0]
    
    if q.vote_casted == True:
        request.session['user'] == -1
        return render(request, 'polls/index.html', {'error': "Sorry this user has already voted"})

    qset = User.objects.all()
    lst_PM = []
    lst_mayor = []
    lst_councillor = []
    for q in qset:
        if q.is_nominated_PM == True:
            lst_PM.append(q.email)
        if q.is_nominated_mayor == True:
            lst_mayor.append(q.email)
        if q.is_nominated_councillor == True:
            lst_councillor.append(q.email)
    
    
    template = loader.get_template('polls/votepage.html')

    return HttpResponse(template.render(context={'user': request.session['user'], 'lst_PM': lst_PM, 'lst_mayor': lst_mayor, 'lst_councillor': lst_councillor }))



@csrf_exempt
def vote(request):
    print(request)
    
    if 'user' not in request.session or request.session['user'] == -1:
        return render(request, 'polls/index.html', {})
    
    print(2)
    qset = User.objects.filter(email=request.session['user'])[0];

    print(qset.email)

    qset.vote_casted = True
    qset.save()

    print(qset.vote_casted)
    print("=============")
    print(qset.email)
    
    #request.session['user'] = -1

    return redirect('/polls/result', context={'error': "Sorry this user has already voted"})

import requests
def result(request):
    r = requests.get('http://localhost:4040/result')
    print(r.json())
    r = r.json()

    for i in r["Stat"]:
        print(i["CatName"])

        if i["CatName"] == "PM":
            print("====================")
            #tmpl = PM(email="a", vote_count=1)
            tmp1 = PM(email=i["UserName"], vote_count=i["Count"])
            tmp1.save()
        elif i["CatName"] == "Mayor":
            tmp1 = Mayor(email=i["UserName"], vote_count=i["Count"])
            tmp1.save()
        elif i["CatName"] == "Councillor":
            tmp1 = Councillor(email=i["UserName"], vote_count=i["Count"])
            tmp1.save()

    for i in r["Result"]:
        print(i["Cat"])
        print(i["Win"])
        print(i["Count"])
        print("")

    
        

    return render(request, 'polls/result.html', {'result': r})
    

def logout(request):
    request.session['user'] = -1
    return redirect("/polls/")
    