from django.shortcuts import render

def home(requеst):
    return render(requеst, 'todo/home.html')
