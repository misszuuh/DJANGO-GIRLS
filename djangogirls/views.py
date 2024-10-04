from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,template_name='djangogirls/base.html')

def community(request):
    return render(request,template_name='djangogirls/community.html')

def resources(request):
    return render(request,template_name='djangogirls/resources.html')