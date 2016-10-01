from django.shortcuts import render
from django.http import HttpResponse

from commando.models import *
# Create your views here.

def home(request):
	all_items = Item.objects.all()
	return render(request, 'commando/index.html', {'items':all_items})

def add_item(request):
	errors = []
	items = Item.objects.all()
	if not 'command' in request.POST or not request.POST['command']:
		errors.append('Missing command')
	elif not 'description' in request.POST or not request.POST['description']:
		errors.append('Missing description')
	elif not 'category' in request.POST or not request.POST['category']:
		errors.append('Missing category')
	else:
		new_item = Item(command = request.POST['command'], description = request.POST['description'], category = request.POST['category'])
		new_item.save()

		items = Item.objects.all()
	context = {'items':items , 'errors':errors}
	return render(request, 'commando/index.html', context)
def index(request):
	return HttpResponse("Hello World");