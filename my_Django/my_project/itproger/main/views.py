from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from .models import *
from .forms import *

# Create your views here.

def index(request):
    return render(request,'main/base.html')

def calc(request):
    summ = ''
    my_list = ['-','+','/','*']
    if request.method == 'POST':
        if request.POST.get('f_num').isdigit() \
            and request.POST.get('l_num').isdigit() \
            and request.POST.get('symbol') in my_list:
            fnum = request.POST.get('f_num')
            symbol = request.POST.get('symbol')
            lnum = request.POST.get('l_num')
            if symbol == '+':
                summ = int(fnum)+int(lnum)
            elif symbol == '-':
                summ = int(fnum)-int(lnum)
            elif symbol == '*':
                summ = int(fnum)*int(lnum)
            elif symbol == '/':
                summ = int(fnum)/int(lnum)
        else:
            return render(request,'main/calc.html',{'sum':'please be careful, incorrect input'})
    return render(request,'main/calc.html',{'sum':summ})

def game(request):
    return render(request,'main/game.html')

def Add_Quest(request):
    if request.method == 'POST':
        quests = request.POST.get('addquest')
        answerss = request.POST.get('answers')
        correct_answers = request.POST.get('correct_answer')
        obj = Add_quests(quest=quests,answers=answerss,correct_answer=correct_answers)
        obj.save()
    return render(request,'main/addquest.html')

def Play_Game(request):
    e = Add_quests.objects.get(id=8)
    answer = e.answers.split(',')
    quest = e.quest
    correct_answers = e.correct_answer
    info=''
    print(correct_answers)
    print(quest)
    print(type(answer))
    if request.method == 'POST':
        if request.POST.get('answer') == correct_answers:
            info = 'right'
        else:
            info = 'wright'
    return render(request,'main/mill.html',{'answer':answer,'quest':quest,'correct_answer':correct_answers,'info':info})

