from django.shortcuts import render

# Create your views here.

def listarods(request):
	return render(request,'ods/ods1.html')