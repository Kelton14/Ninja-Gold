from django.shortcuts import render, redirect, HttpResponse
import random
from time import localtime, strftime

def index(request):

    if 'total' not in request.session:
        request.session['total'] = 0

    if 'number' not in request.session:
        request.session['number'] = 0

    if 'result' not in request.session:
        request.session['result'] = []

    context = {
        "total" : request.session['total'],
        "number" : request.session['number'],
        "result" : request.session['result'],
    }

    return render(request, 'index.html', context)

def process_money(request) :
    if 'total' in request.session: 
        if request.POST['totalb'] == 'farm':
            request.session['number'] = random.randint(10, 20) 
            request.session['total'] += request.session['number']
            time = strftime('%I:%M %p, %m %d, %Y')
            number = request.session ['number'] 
            results = f' Earned {number} from the Farm {time}'
            request.session['result'].append(results)
    if 'total' in request.session: 
        if request.POST['totalb'] == 'cave':
            request.session['number'] = random.randint(5, 10)
            request.session['total'] += request.session['number']
            time = strftime('%I:%M %p, %m %d, %Y')
            number = request.session ['number'] 
            results = f' Earned {number} from the Cave {time}'
            request.session['result'].append(results)
    if 'total' in request.session: 
        if request.POST['totalb'] == 'house':
            request.session['number'] = random.randint(2, 5)
            request.session['total'] += request.session['number']
            time = strftime('%I:%M %p, %m %d, %Y')
            number = request.session ['number'] 
            results = f' Earned {number} from the House {time}'
            request.session['result'].append(results)
    if 'total' in request.session: 
        if request.POST['totalb'] == 'casino':
            request.session['number'] = random.randint(-50, 50)
            request.session['total'] += request.session['number']
            if request.session['number'] > 0:
                time = strftime('%I:%M %p, %m %d, %Y')
                number = request.session ['number'] 
                results = f' Earned {number} from the Casino {time}'
                request.session['result'].append(results)
            if request.session['number'] < 0:
                time = strftime('%I:%M %p, %m %d, %Y')
                number = request.session ['number'] 
                results = f' Lost {number} from the Casino {time}'
                request.session['result'].append(results)

    return redirect('/')

def destroy_session(request):
    request.session.clear()
    return redirect('/')


