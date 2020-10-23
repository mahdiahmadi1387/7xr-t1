from django.shortcuts import render

def home(request):
    return render(request,'booksapp/home.html')