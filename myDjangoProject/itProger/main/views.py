from django.shortcuts import render
from django.views.generic import TemplateView
from django.db import connection
from .models import *
import random

# Create your views here.

my_list = []

class index(TemplateView):
    template_name = "main/base.html"

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
    global my_list
    info=''
    posts = Add_quests.objects.all()
    num = random.randrange(len(posts))
    answers = posts[num].answers.split(',')
    quest = posts[num].quest
    correct_answer = posts[num].correct_answer
    if request.method == 'POST':
        if request.POST.get('answer') == correct_answer:
            info = 'right'
        else:
            info = 'wrong'
    return render(request,'main/mill.html',{'answers':answers,'quest':quest,'correct_answer':correct_answer,'info':info})
