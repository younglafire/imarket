from django.shortcuts import render

def index(request):
    return render(request, 'index.html')  # adjust template path if needed