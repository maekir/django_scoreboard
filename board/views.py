from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic
from board.forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormMixin
from board.models import Racer, Race, Comment
from board.forms import CommentForm
from django.contrib.auth.models import User

def index(request):
    num_racers = Racer.objects.all().count()
    num_races = Race.objects.all().count()  
    context = {
        'num_racers': num_racers,
        'num_races': num_races,
    }
    return render(request, 'index.html', context=context)


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    context = {
        'user_form':user_form,
        'registered':registered
    }
    return render(request,'board/registration.html', context)


def races_list(request):
    races = Race.objects.all()
    context = {
        "races": races,
    }
    return render(request, 'board/races_list.html', context)


def race_detail(request, id):
    race = Race.objects.get(id=id)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                commenter = request.user,
                race = race,
                text = form.data["text"],
                type = form.data["type"]
            )
            comment.save()
    comments = Comment.objects.filter(race=race)
    context = {
        "race": race,
        "comments": comments,
        "form": form,
    }
    return render(request, "board/race_detail.html", context)
