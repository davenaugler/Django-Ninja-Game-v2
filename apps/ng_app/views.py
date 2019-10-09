from django.shortcuts import render, redirect
from random import randint
from datetime import datetime
from time import strftime

# Create your views here.
def index(request):
    if 'count_down' not in request.session:
        request.session['count_down'] = 15
        request.session['button'] = ''
        request.session['text'] = ''
        request.session['action'] = ''
    return render(request, 'ng_app/index.html')

def process_money(request):
    property = request.POST['property']
    now = datetime.now()
    date_now=now.strftime("%Y/%m/%d %I:%M %p")
    if 'gold' not in request.session:
        request.session['gold'] = 0
        request.session['activities'] = ''

    if request.POST['property'] == 'farm':
        gold = randint(10,20)
        request.session['gold'] += gold
        request.session['count_down'] -= 1
        print('Recieved [', gold,'] golds from the Farm for a total of', request.session['gold'], 'golds')
    elif request.POST['property'] == 'cave':
        gold = randint(5,10)
        request.session['gold'] += gold
        request.session['count_down'] -= 1
        print('Recieved [', gold,'] golds from the Cave for a total of', request.session['gold'], 'golds')
    elif request.POST['property'] == 'house':
        gold = randint(2,5)
        request.session['gold'] += gold
        request.session['count_down'] -= 1
        print('Recieved [', gold,'] golds from the House for a total of', request.session['gold'], 'golds')
    else:
        request.POST['property'] == 'casino'
        gold = randint(-50,50)
        request.session['gold'] += gold
        request.session['count_down'] -= 1
        print('Recieved [', gold,'] golds from the Casion for a total of', request.session['gold'], 'golds')

    if request.session['count_down'] == 0:
        request.session['button'] = "<button type='submit' class='btn btn-lg btn-block btn-danger bigger-text mt-5 p-3 {{ request.session.button }}'>Reset</button>"
        request.session['text'] = 'Reset'
        request.session['action'] = 'reset'


    if request.session['count_down'] == 0:
        request.session['count_down'] = "<span class='text-danger'>You loose. Let's play again!</span>"
        
    if gold < 0:
        request.session['activities'] = "<li class='text-danger' style='list-style-type:none'>Entered a casino and lost " +str(gold)+ " golds...Ouch! ("+ date_now +")" + request.session['activities']+"</li>"
    else:
        request.session['activities'] = "<li class='text-success' style='list-style-type:none'>Earned " +str(gold)+ " golds from the " +property+ "! ("+ date_now +")" + request.session['activities']+"</li>"  
    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')