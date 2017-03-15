from django.template.loader import get_template 
from django.template import Context 
from django.http import HttpResponse 
import datetime 

def index(request):
	t = get_template('index.html') 
	html = t.render(Context()) 
	return HttpResponse(html) 

def hello(request): 
    return HttpResponse("Hello  xxx world") 

def current_datetime(request):
	now = datetime.datetime.now()
	t = get_template('current_datetime.html') 
	html = t.render(Context({'current_date': now})) 
	return HttpResponse(html) 
