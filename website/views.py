from django.shortcuts import render,redirect
from django.contrib import messages

from .models import User, Comment, NewVideo
from django.http import HttpResponseRedirect
from datetime import date
from django.db.models import Q


from django.views.generic import TemplateView,ListView

class HomePageView(TemplateView):
    template_name = 'home.html'


def homepage(request):
    return render(request,'homepage.html')


def video(request):
    return render(request,'videoView.html')
       


def upload(request):
    return render(request,'upload.html',{})

