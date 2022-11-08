from django.shortcuts import render
from django.http import HttpResponse,Http404

# Create your views here.

challenges = {
    'January':'No Thumbs!',
    'February':'The other hand!',
    'March':'Pick it up with your feet!',
    'April':'Build a house of cards!',
    'May':'Seven second games',
    'June':'Catch coins!',
    'July':'Can you wiggle your face!',
    'August':'Different accents!',
    'September':'Blindfold',
    'October':'One minute games',
    'November':'Not my arms',
    'December':'Guess who'
}

def index(request,challenge):
    
    try:
        check = challenges[challenge]
        return render(request,'challenges/view.html',context=challenges)
    except:
        raise Http404("404 GENERIC ERROR")