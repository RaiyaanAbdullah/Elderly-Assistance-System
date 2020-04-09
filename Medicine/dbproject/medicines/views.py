from django.shortcuts import render
from django.http import HttpResponse
from .models import medicine
# Create your views here.

def medicine_data(request):
	obj=medicine.objects.all()
	content={
			'object': obj

	}

	return render(request,'Medicine.html',content)





