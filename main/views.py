from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import *
from study.models import *
from study.models import study
from django.utils import timezone

# Create your views here.


def showmain(request):
    posts = study.objects.all()
    return render(request, 'main/index.html', {
        'posts': posts,
    })
