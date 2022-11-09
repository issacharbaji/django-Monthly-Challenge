from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse

# Create your views here.


challenges = {
    'my_dic': {'January': 'No Thumbs!',
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
               'December': 'Guess who', }
}


def home(request):

    return render(request, 'challenges/view.html', context=challenges)


def index(request, month):

    try:
        result = challenges['my_dic'][month]
        return HttpResponse(result)
        # return render(request,'challenges/view.html',context= challenges)
    except:

        raise Http404()


def month_num(request, num):

    key_list = list(challenges['my_dic'])  # a list of the months

    if num > len(key_list):
        raise Http404()

    month = key_list[num - 1]
    redirect_path = reverse('month_num', args=[month])
    return HttpResponseRedirect(redirect_path)
