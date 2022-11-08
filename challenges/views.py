from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

challenges = {
    'January': 'No Thumbs!',
    'February': 'The other hand!',
    'March': 'Pick it up with your feet!',
    'April': 'Build a house of cards!',
    'May': 'Seven second games',
    'June': 'Catch coins!',
    'July': 'Can you wiggle your face!',
    'August': 'Different accents!',
    'September': 'Blindfold',
    'October': 'One minute games',
    'November': 'Not my arms',
    'December': 'Guess who',
}


def index(request, month):

    try:
        result = challenges[month]
        return HttpResponse(result)
        # return render(request,'challenges/view.html',context= challenges)
    except:
        result = 'No page for this topic'
        raise Http404("404 GENERIC ERROR")


def month_num(request, num):

    key_list = list(challenges.keys())  # a list of the months

    if num > len(key_list):
        return HttpResponse('Invalid month')

    month = key_list[num - 1] 
    redirect_path = reverse('month_num', args=[month])
    return HttpResponseRedirect(redirect_path)
