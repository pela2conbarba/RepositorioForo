from django.shortcuts import render

# Create your views here.

def listarblog(request):
	return render(request,'blog/index.html')