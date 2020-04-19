from django.shortcuts import render
from django.http import HttpResponse
from .models import report
from django.template import loader

# Create your views here.
def index(request):
    latest_news = report.objects.order_by('-pub_date')
    template = loader.get_template('news/index.html')
    context = {
        'latest_news': latest_news,
        }
    return HttpResponse(template.render(context, request))
    #return render(request, 'news/index.html' )