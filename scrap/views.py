from django.shortcuts import render,get_object_or_404
from . import incometax
from .models import Notif
#from django.urls import reverse
#from django.http import HttpResponseRedirect
from dateutil.parser import parse
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
#from django.views.generic import ListView
    
    
def home(request):
    return render(request,'scrap/home.html')

def get_data(request):
    
    data = incometax.incometax_data()
    y = Notif.objects.all()
    count = 0    
    if(y.exists()):
        notice = Notif.objects.all().order_by('-publish')[0]
        date = notice.publish
        for x in data:
            if(parse(x[2]) > date):
                notice = Notif(title=x[0],
                               link = ('https://www.incometaxindia.gov.in'+x[1]),
                               publish=parse(x[2]),
                               info = x[3])
                notice.save()
                count = count+1
        
    else:
        for x in data:
            notice = Notif(title=x[0],
                           link = ('https://www.incometaxindia.gov.in')+x[1],
                           publish=parse(x[2]),
                           info = x[3])
            notice.save()
            count = count+1
        
    messages.info(request, 'Records are Updated Succesfully!')
    
    return render(request, 'scrap/home.html', {'count': count})



def show_data(request):
    object_list = Notif.objects.all().order_by('-publish')
    paginator = Paginator(object_list,7) # 5 notices in each page
    page = request.GET.get('page')
    try:
        notices = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        notices = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        notices = paginator.page(paginator.num_pages)
    return render(request,
                  'scrap/incometax/show.html',
                  {'page': page,
                   'notices':notices})
